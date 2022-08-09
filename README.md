# kafka-mac-experiment

Experimenting with Kafka on Mac

## Setup

- Install java +8
	- `brew cask install java`
- Install scala 2.13
	- `brew install coursier/formulas/coursier && cs setup`
- Install python 3.10
	- Install pyenv
- Install python libraries
	- ~~`pip install faust=1.10.4`~~ Incompatible with python 3.10 `TypeError: As of 3.10, the *loop* parameter was removed from ThrowableQueue() since it is no longer necessary`
    - `pip install python3-kafka`
- Install kafka
	- `brew install kafka`
- Start zookeeper
	- `zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties`
- Configure kafka server
	- `vim /usr/local/etc/kafka/server.properties`
	- Uncomment `listeners=PLAINTEXT://:9092`
- Start kafka server
	- `kafka-server-start /usr/local/etc/kafka/server.properties`
- Create test topic
	- `kafka-topics --create --topic test --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`
- Initialize producer console and send a few messages
	- `kafka-console-producer --broker-list localhost:9092 --topic test`
- Initialize consumer console to receive messages
	- `kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning`
- Run python script
    - `python test.py`

## Notes
- To reset kafka after an upgrade
	- `brew services restart kafka`

