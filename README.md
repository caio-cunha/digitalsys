# Sistema de Propostas de Emprestímos

Application to register/edit/delete grant proposals.
***

## Quick Reference

   - [Requirements](#requirements);
   - [Installation](#installation);
   - [Running the project](#running-the-project);
***

## Requirements

To run the application are required the following dependecies:

    - [Docker](https://docs.docker.com/);
    - [Docker compose](https://docs.docker.com/compose/gettingstarted/);

***

## Installation

1. Clone the application repository, running the following command:

```bash
git clone https://github.com/caio-cunha/digitalsys.git #for HTTPS method
#or
git clone git@github.com:caio-cunha/digitalsys.git #for SSH method
```

2. Change the project permissions:

```bash
cd digitalsys/
sudo chown -R $USER:$USER .
```
***

## Running the project

1. Before to execute the commands bellow, create the local.env with base in local.example.env:

```bash
cp app/app/local.example.env app/app/local.env
cd ..
cd ..
```

2. Executation of the application:

```bash
sudo bash ./scripts/run-dev.sh up # Up the docker containers
sudo bash ./scripts/run-dev.sh upd # Up the docker containers as daemon mode
```

3. Enter in djang-admin:

```bash
localhost:8000/admin
user: admin
password: 123456
```

4. Enter in frontend application:

```bash
localhost:8000
```

5. Enter in swagger (documantation):

```bash
localhost:8000/swagger
```
