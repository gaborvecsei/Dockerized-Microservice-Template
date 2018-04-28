# Microservice Template with Docker

This is a small project where the following is combined in order to create a usable microservice:

- [RestAPI (Python + Flask)](https://github.com/pallets/flask)
- [Postgres Database](https://www.postgresql.org/)
- [Nginx](https://www.nginx.com/)
- [Postgres db explorer](http://sosedoff.github.io/pgweb/) (This can be removed, it is only used for testing)

## Test it

- Clone and start it:

```sh
git clone https://github.com/gaborvecsei/Dockerized-Microservice-Template.git

sudo ./start.sh
```

- Stop it:

```sh
sudo docker-compose down
```

- See the container logs:

```sh
sudo docker-compose logs -f
```

## TODO

- [ ] Log In
- [ ] User Page
- [ ] Registration
- [ ] Billing (Buying units)