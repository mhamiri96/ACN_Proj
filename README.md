# Weighted Fair Queuing Scheduling

## Intro
Weighted Fair Queuing (WFQ) offers fair queuing
that divides the available bandwidth across queues of
traffic based on weights. Each flow or aggregate thereof is
associated with an independent queue assigned with a
weight, so as to ensure that important traffic gets higher
priority over less important traffic. In times of congestion
the traffic in each queue (a single flow or an aggregate of
them) is protected and treated fairly, according to its
weight.
Arriving packets are classified into different queues by
inspection of the packet header fields, including
characteristics such as source and destination network or
MAC address, protocol, source and destination port and
socket numbers of the session or Diff-Serv-Code-Point (DSCP) value. Each queue shares the transmission service
proportionally to the associated weight. All traffic in the
same class is treated indistinctly.
## Desirable Properties
In summary, from a technical point of view WFQ has
three desirable properties. First, because it approximates
GPS (General Processor Sharing) scheduler, it protects
traffic of different queues from each other, which is
fundamental in a service differentiation context. Second,
traffic in a queue can obtain worst-case end-to-end
queuing delay that is independent of the number of hops it
traverses and of the behavior of traffic in the other queues.
This allows networks of fair queuing schedulers to provide
real-time performance guarantees. Third, it gives users an
incentive to implement intelligent flow mechanisms at the
end-system. A source is not required to send at a rate
smaller than its currently allocated rate, however if it sends
more than its fair share it can lose packets, so it has an
incentive to match its flow to the currently available
service rate.

## Process OF WFQ
It has kind of **estimated finish time** based on some **predifined weights** and also with each weight, it has its **own and separate queue**. 
Therefore, there is a scheduler which selects the packet with earliest estimated finish time to be transmitted while preserving prioritization and fairness.

## How to run code 
### **Configuration**

- **init[number of testing scenario].csv** : each row contains info about a flow which respectively cosists of 1. weight of flow, 2. number of flow, 3. average time interval of packets, 4. average length of packets and 5. number of packets.
- By adding or deleting rows or changing these five elements, you can be flexible about the functionality of this application.
- The time interval of packets is uniformly assigned which means for example, by interval of 0.5 second, the packets will be send.
- The length of packets is assigned by Gaussian distribution and with setting 4 parameter in this file, the mean of this distribution has been determined and by default, the standard deviation is hard coded and is 50.

### **Run code**
  - **step 1 :** after setting your configs in **init[number of testing scenario].csv** file, you should run **router.py** file (```python router.py [number of testing scenario]```).
  - **step 2 :** then you need to run **dest.py** file (```python dest.py```).
  - **step 3 :** at last, you just need to run **makefile** (```make```) or you can run as many as you like **source.py** file with your configs but corrsponding flow should be as same as one of the rows of **init[number of testing scenario].csv** file (```python source.py 0 0.5 100 100```).
=======
  - **step 3 :** at last, you just need to run **makefile** (```make```) **but** you should consider that for each scenario you might need some changes in ```makefile``` (for example, you have 4 flows and the requirments of the flow is initialized and written down in **init[number of testing scenario].csv**, then you need to check the ```makefile``` if the first line has 4 instances and also by following, it has 4 commands with corresponding flow's info) or you can run as many as you like **source.py** file with your configs but corrsponding flow should be as same as one of the rows of **init[number of testing scenario].csv** file (for example```python source.py 0 0.5 100 100```).
  - All these commands need to be run in terminal with the same path of the project's path.
## About files
All communcations are handled by socket programming.
- **source.py** : by using gaussian distribution, the length of each packet is generated randomly. Also, in this file, sending packets which corrspond to its own flow is been considered.
- **dest.py** : This file contains info about destination and all packets of flows will be transmitted here.
- **main.py** : It gets some configs from init.csv and also make ready other info which will be used in router.py
- **router.py** : In this file, threading has been considered. We have two threads, one for recieving packets and the other on for sending packets. ```recvpacket()``` function consisted of WFQ scheduling and assigning and calculating round number and finished number of packets and putting packets in its own queue. 

## Results
Results can be visible in terminals of router.py, dest.py and makefile and for checking the output result of router, you need to check log of dest.py file.
## Contributing
Contributions and feedback on the WFQ scheduling and its applications in computer networking are welcomed. 

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
