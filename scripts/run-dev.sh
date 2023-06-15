#!/bin/sh

case "$1" in
        
        upd)
                echo "Up Daemon ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml up -d
                ;;
        
        up)
                echo "Up ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml up 
                ;;

        down)
                echo "Down ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml down
                ;;

        down-volume)
                echo "Down ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml down -v
                ;;
        logs)
                echo "Logs ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml logs -f
                ;;

        build)
                echo "build ..."
                DUID=$(id -u) DGID=$(id -g) docker-compose -f $(pwd)/docker-compose.yml build
                ;;

esac