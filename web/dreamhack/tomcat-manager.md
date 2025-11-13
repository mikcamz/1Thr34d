# Tomcat Manager
This challenge involves leaking credential with LFI and RCE with webshell

## Solve
### Leaking cred
Unzipping the `ROOT.war` file and look at `image.jsp` we can see that there are no filter against path => LFI and read `tomcat-users.xml` (contain cred and role) with this url: (location is seen from docker file: `COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml`

![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/eef71b33dfada4543953d129379f1547d66e390a1f0214a760ddae2617708952.png)

### Accessing /manager
Using the cred collected (`tomcat:P2assw0rd_4_t0mC2tM2nag3r31337`) to login into /manager

![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/48fb266e80da1205d426883532761e1afbccb531ffaa53ee53d4d7aab8979123.png)

We get access to /manager endpoint, which is a dashboard of tomcat. The user `tomcat` have this permission since it have the `manager-gui` role defined in tomcat-users.xml:
```
<user username="tomcat" password="[**SECRET**]" roles="manager-gui,manager-script,manager-jmx,manager-status,admin-gui,admin-script" />  
```

![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/3c083dffccf848c57274ad9d62c9a31765fc1f09b0022886c4a7a8037e3bd7a8.png)

From this i used this github repo webshell.war file to upload using the tomcat /manager page: https://github.com/p0dalirius/Tomcat-webshell-application.
Access the endpoint i just upload and execute the flag binary at `/flag`
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/b055d6abd15588b280154622ac3f1d49e0273232f7b7140a393c427f5bfc70d0.png)

>NOTE: tomcat user only have execute perm on /flag, this is why we can't directly leak the flag with LFI from the last section
>![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/9f802fc827133f7066d3d5b9ca5b8c149a4042d3eb979975119d074fab70112a.png)
