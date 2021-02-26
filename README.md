# Eletronicx FullStack Challenge 🤯🤯🤯
This is a public repository with contents of Flask Web Development, NextJS and Typescript, here you will find examples applied in a Restful API, and a basic and flexible structure to start your Flask apps. Also, is available a complete frontend in NextJS + Typescript, ready to consume our backend API
<br />
<h1>Steps to run this app 👇👇👇</h1>
<br />

1- Cloning repo
-----------------------------------

```
$ git clone https://github.com/josethz00/eletronicx_fullstack
```

2- Enter in folder (server)
-----------------------------------

```
$ cd server
```

3- Run the container
-----------------------------------

```
$ docker-compose up --build --remove-orphans
```

4- Run tests into the container
-----------------------------------

```
$ docker exec -it flask_app_container python3 -m pytest __tests__ -v
```

5- Enter in folder (web)
-----------------------------------

```
$ cd ../web
```

6- Install the dependencies
-----------------------------------

```
$ yarn install
```

7- Start the web app
-----------------------------------

```
$ yarn start
```

<br />

## Check some of the default env variables (available on ``` server/config/variables.py ```)

| Env Variable  | Default Value |
| ------------- | ------------- |
| HOST  | '0.0.0.0'  |
| PORT  | '5000' |
| DEBUG | 'True' |
