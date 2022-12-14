## BOBI-FE

```
๐ FE
โโbobi_frontend			// ํ์ฌ ๋ฐฐํฌ๋์ด์๋ ์๋ฒ ๊ธฐ์ค
โโDOCS						
โโtest					// ๋ก์ปฌ ํ์คํธ์ฉ (mqtt ๋ฑ)
```



## ํ๊ฒฝ

- ECMAScript 6 ๊ธฐ๋ฐ์ ์นํ์ด์ง

- PWA๋ฅผ ํ์ฉํ ์น์ฑ ํํ

  

## ์ฌ์  ์ค๋น

1. CRA๋ฅผ ์ด์ฉํด์ ๋ฐ๋ก webpack ์ค์ ์์ด ํ๋ก ํธ์๋ ๊ฐ๋ฐํ๊ฒฝ ์ค์ 
2. React 18.2.0

```jsx
$ git clone <https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A208.git>
$ git switch FE
$ cd FE
$ cd bobi_frontend
$ npm i --force
$ npm start
```



## ์ฌ์ฉํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ

1. ๋ฐ์ํ ์น ํ์ด์ง

- react-router-dom 6.3.0

1. ๊ตฌ๊ธ ๋ก๊ทธ์ธ

- react-google-login 5.2.2
- gapi-script 1.2.0

1. mqtt ํต์ 

- mqtt 4.3.7

1. S3 ์๋ก๋

- react-s3 1.3.1

1. ์์ฑ ์ฌ์ ํ๋ ์ด์ด

- react-player 2.10.1

1. ์ผ์ ๊ฐ ๊ทธ๋ํ

- react-apexcharts 1.4.0

1. ์ด๋ชจํฐ์ฝ

- @fortawesome/react-fontawesome 0.2.0

- @fortawesome/free-solid-svg-icons 6.1.2

  

# Web to S3, S3 to Web Authorization

> S3 ๋ฒํท ์์ฑ์ ๋งํฌ(์ถ๊ฐ์์ ) ์ฐธ์กฐ

1. ๋ฒํท์ ๋ด๋ถ์ ๊ถํ ํญ ์ด๋

   ![image-20220818001735534](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001735534.png)



2. ํผ๋ธ๋ฆญ ์ก์ธ์ค ์ฐจ๋จ ํธ์ง

![image-20220818001751104](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001751104.png)

๋ชจ๋  ์ฐจ๋จ ํด์ ํ๊ธฐ

![image-20220818001808131](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001808131.png)



3. ๋ฒํท ์ ์ฑ ์์ ํ๊ธฐ

![image-20220818001835111](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001835111.png)



ํธ์ง์ ํด๋ฆญํ๊ณ  ์๋์ ๊ฐ์ด ์๋ ฅํ๊ณ  ๋ณ๊ฒฝ์ฌํญ ์ ์ฅ

```jsx
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "PublicReadGetObject",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::bobivoicebucket/*"
		}
	]
}
```



4. CORS ์ ์ฑ ์์ ํ๊ธฐ

```jsx
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "HEAD",
            "POST",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin",
            "x-amz-server-side-encryption",
            "x-amz-request-id",
            "x-amz-id-2"
        ]
    }
]
```

5. ์ก์ธ์ค ํค ๋ฐ๊ธ๋ฐ๊ธฐ

์ฐ์ธก ์๋จ ๋ณด์์๊ฒฉ์ฆ๋ช ์ด๋

![image-20220818001912095](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001912095.png)

ํธ์ง์ ํด๋ฆญํ๊ณ  ์๋์ ๊ฐ์ด ์๋ ฅํ๊ณ  ๋ณ๊ฒฝ์ฌํญ์ ์ฅ

![image-20220818001926919](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001926919.png)

์ก์ธ์ค ๊ด๋ฆฌ - ์ฌ์ฉ์ ํญ ์ด๋

![image-20220818001939969](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001939969.png)

Administrator ์ด๋

![image-20220818001952585](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818001952585.png)

๋ณด์ ์๊ฒฉ ์ฆ๋ช ํญ ์ด๋

![image-20220818002004019](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002004019.png)

Access Key ๋ง๋ค๊ณ  Access Key, Secret Access Key๊ฐ ๊ธฐ๋กํ๊ธฐ (์ก์ธ์ค ํค๋ 2๊ฐ๊น์ง ๋ฐ์ ์ ์์ด์ ํ์ฌ๋ ๋นํ์ฑํ ์ํ)

![image-20220818002019001](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002019001.png)

```jsx
import { uploadFile } from "react-s3";

...

const config = {
  bucketName: S3_BUCKET,
  region: REGION,
  accessKeyId: ACCESS_KEY,
  secretAccessKey: SECRET_ACCESS_KEY,
};

...

uploadFile(file, config)
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
```

7. ๋ค์ด๋ก๋ ํ  ๋

![image-20220818165731562](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220818165731562.png)





![image-20220818165741537](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220818165741537.png)



# ๊ตฌ๊ธ ๋ก๊ทธ์ธ (ํด๋ผ์ด์ธํธ์ฌ์ด๋)

1. ๊ตฌ๊ธ ํด๋ผ์ฐ๋ ํ๋ซํผ ์ ์ํด์ ๋ก๊ทธ์ธํ๊ธฐ https://console.cloud.google.com/
2. ์ ํ๋ก์ ํธ ์์ฑ

![image-20220818002105200](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002105200.png)

![image-20220818002113044](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002113044.png)



3. ํ๋ก์ ํธ ํญ ๋ค์ ํด๋ฆญํด์ ์์ฑํ ํ๋ก์ ํธ๋ก ์ด๋ํ๊ธฐ

![image-20220818002133673](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002133673.png)



4. ์ฌ์ฉ์ ์ธ์ฆ ์ ๋ณด๋ก ์ด๋

![image-20220818002153195](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002153195.png)

5. OAuth ํด๋ผ์ด์ธํธ ID ๋ฐ๊ธ๋ฐ๊ธฐ

![image-20220818002206552](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002206552.png)

6. ์ ํ๋ฆฌ์ผ์ด์ ์ ํ ์ ํ๊ธฐ

![image-20220818002227749](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002227749.png)

7. ์ด๋ฆ ์๋ ฅํ๊ณ  ๊ตฌ๊ธ ๋ก๊ทธ์ธ ์ ์ฉํ  ์ฌ์ดํธ URI ์ฐ๊ณ  ๋ฆฌ๋๋ ์ URI ์๋ ฅํ๊ธฐ

![image-20220818002241595](C:\Users\SSAFY\Desktop\S07P12A208\FE\README.assets\image-20220818002241595.png)

1. ์น์ ์ ์ฉํ๊ธฐ

```jsx
import { GoogleLogin } from "react-google-login";
import { gapi } from "gapi-script";

...

const googleClientId = process.env.REACT_APP_GOOGLE_API_KEY;

useEffect(() => {
  function start() {
    gapi.client.init({
      clientId: googleClientId,
      scope: "email",
    });
  }
  gapi.load("client:auth2", start);
}, []);

const onSuccess = (response) => {
  // ๋ก๊ทธ์ธ ์ฑ๊ณตํ์ ๋ ์คํํ  ํจ์
};

const onFailure = (response) => {
	// ๋ก๊ทธ์ธ ์คํจํ์ ๋ ์คํํ  ํจ์
};

<GoogleLogin
  clientId={googleClientId}
  onSuccess={onSuccess}
  onFailure={onFailure}
/>
```



react-google-login์ ์๋  ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ผ์ ๊ทธ๋ฐ์ง npm install ํ  ๋๋ง๋ค ๋นจ๊ฐ ์ค๋ฅ๊ฐ ์๊พธ ๋จ๋๋ฐ ๋ค๋ฅธ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ก ๋์ฒด ๊ถ์ฅ

###### Tech Stack

- React





>>>>>>> e093068866a1e97bf6af0376e0c88635ec9e224c
