# AWS- Skill Alexa (Ensine frases a alexa)

Skill consuming the aws service, Skill that learns phrases, remembers and returns intelligently. 

<p align="center">
  <img width="860" height="500" src="https://user-images.githubusercontent.com/66971579/84856886-34e36480-b03e-11ea-95ec-b72097506395.jpeg">
</p>



### Requirements

The requirements to run such an application are linked to the infrastructure of amazon skil kits, it being necessary to create an account on the same console, in hardware matters a machine with 2gb of ram and few open pages can run smoothly, taking into account that the amazon own web service for code development.

```
2gb ram - intel processor inside or parallel to it - windows operating system - vs code - python3.7 or higher
account on the platform
```





### Getting Started

To get started, log in to [Alexa developer console](https://developer.amazon.com/alexa/console/ask) with your Amazon Developer account. If you don't have an account, [clique aqui](https://www.amazon.com/ap/register?clientContext=131-0331464-9465436&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&siteState=clientContext%3D142-6935021-1894360%2CsourceUrl%3Dhttps%253A%252F%252Fdeveloper.amazon.com%252Falexa%2Csignature%3Doyixlki7Yxz8bRUtt4vGJ4EugQ8j3D&marketPlaceId=ATVPDKIKX0DER&language=en_US&pageId=amzn_developer_portal&openid.return_to=https%3A%2F%2Fdeveloper.amazon.com%2Falexa&prevRID=HSRBQ1KHA4E5D1PBHPPP&openid.assoc_handle=mas_dev_portal&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0) to create one.

<p align="center">
  <img width="460" height="250" src="https://user-images.githubusercontent.com/66971579/84858613-e6d06000-b041-11ea-98ce-0b30825f5de3.jpeg">
</p>







## Running 0.1

After creating the account look for the console button located in some corner of the screen it may be different from the image below because amazon modifies the website design constantly for a better user experience.

<p align="center">
  <img width="660" height="350" src="https://user-images.githubusercontent.com/66971579/84859044-b0471500-b042-11ea-81fe-82c9a4dac619.jpeg">
</p>




## Running 0.2

Now look for the area written "code" to go to the development area.

<p align="center">
  <img width="660" height="350" src="https://user-images.githubusercontent.com/66971579/84859656-f8b30280-b043-11ea-870a-9d60fd06201d.jpeg">
</p>



At this point you should add the code in all areas for the code to work properly, note that the lambda file contains the files:
* lambda-function.py
* requeriments.txt
* utils.py

<p align="center">
  <img width="660" height="350" src="https://user-images.githubusercontent.com/66971579/84861616-db803300-b047-11ea-90bb-480d38d11292.jpeg">
</p>
It is necessary to import additions correctly so that the S3 storage can receive the data correctly.


## Importante ressaltar

I chose to use all the service indicated on amazon sdk as a database, json etc ... but there is the option to use other banks in my readings I found a lot about dynamoDB it is offered by Amazon as part of the Amazon Web Services portfolio , however it is possible to use others like mongoDB and parallels. 
 


## Running 0.3


 Now look for the area written "Build" to develop the intents

<p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84859987-9a3a5400-b044-11ea-9395-5084445c78c7.jpeg">
</p>


 Search for the name intents and create a new intent as the images illustrate and exactly as written below, if you find it necessary to modify the name of the intent remember that it must be modified in all the code in the lambda file.
 
 ```
 CaptureRecordindintent
 
 ```
 After creating the intent it will be necessary to develop a call for it, I opted for "unknown" chamala and right after creating phrase options that users can say to interact with the skill.
 <p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84863742-d624e780-b04b-11ea-85e2-e3ee1bac9fd4.jpeg">
</p>



Now it will be necessary to define which type of slot the intent will use, I opted for "AMAZON.SearchQuery" was the one that had the best response and at the time of certification of the skill the architects of aws instructed me to use it.

```
choose slot type: AMAZON.SearchQuery

```

<p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84864161-9d394280-b04c-11ea-9de1-d27204b0b5a7.jpeg">
</p>


## Running 0.4


Now look for the area written "test" to test the skill.

<p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84859236-1f246e00-b043-11ea-99f5-45510a46c5a4.jpeg">
</p>


You will see a test console in the drop-down menu at the top of the page, select Development:

<p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84865031-f35ab580-b04d-11ea-95a8-85b150a09df9.png">
</p>

After that use the call phrases of the skill and it should return that you learned:

<p align="center">
  <img width="660" height="450" src="https://user-images.githubusercontent.com/66971579/84865564-d5418500-b04e-11ea-9faf-8fcb15b5c73d.jpeg">
</p>






### Final considerations 

This is a brief indication and a way to start a simple skill, if you find it difficult to develop it is interesting to consult the guide developed by the website for a better explanation about the console and the services provided by AWS. It is important to pay attention to the code, as the information is directed to the cloud service. If you want to delete the learning that Alex had, you will need to delete the media from the S3 storage. 






