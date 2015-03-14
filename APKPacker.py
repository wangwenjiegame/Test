apktool d -f GravityBoy-release-signed.apk
apktool b GravityBoy-release-signed GravityBoy-unsigned-100000.apk
#Éú³Ékeystore
#keytool -genkey -keystore pingpinggame.keystore -keyalg rsa -alias pingpinggame -validity 20000
jarsigner -keystore C:\Projects\Android\threemusketeers.keystore -storepass wangwenjie -keypass wangwenjie -sigfile CERT -signedjar GravityBoy-signed-100000.apk GravityBoy-unsigned-100000.apk threemusketeers -verbose -certs
C:\adt-bundle-windows-x86_64-20140702\sdk\build-tools\android-4.4W\zipalign.exe -v 4 GravityBoy-signed-100000.apk GravityBoy-release-signed-100000.apk
111