# **Coder Academy - Assignment T1A1 - Workbook: Submitted by Mario Lisbona**

# **Table of contents**

- [**Coder Academy - Assignment T1A1 - Workbook: Submitted by Mario Lisbona**](#coder-academy---assignment-t1a1---workbook-submitted-by-mario-lisbona)
- [**Table of contents**](#table-of-contents)
  - [Question 1 - Web Development Markup Laguages](#question-1---web-development-markup-laguages)
  - [Question 2 - Internet Technologies: Packets, IP, Routers and DNS](#question-2---internet-technologies-packets-ip-routers-and-dns)
  - [Question 3  - Internet Technologies: TCP, HTTP/HTTPS and Web Browsers](#question-3----internet-technologies-tcp-httphttps-and-web-browsers)
  - [Question 4 - Python Data Structures](#question-4---python-data-structures)
  - [Question 5 - Interpreters and Compilers](#question-5---interpreters-and-compilers)
  - [Question 6 - Pros / Cons of Python and JavaScript](#question-6---pros--cons-of-python-and-javascript)
  - [Question 7 - Ethics and Tech](#question-7---ethics-and-tech)
  - [Question 8 - Control Flow in Python](#question-8---control-flow-in-python)
  - [Question 9 - Type Coercion and Type Conversion in Python](#question-9---type-coercion-and-type-conversion-in-python)
  - [Question 10 - Data Types](#question-10---data-types)
  - [Question 11 - Classes](#question-11---classes)
  - [Question 12 - Find the error in a Code Snippet](#question-12---find-the-error-in-a-code-snippet)
  - [Question 13 - Rewrite a Code Snippet to swap two adjacent elements in an list](#question-13---rewrite-a-code-snippet-to-swap-two-adjacent-elements-in-an-list)
  - [Question 14 - Algorithmic Thinking](#question-14---algorithmic-thinking)
  - [Question 15 - Python code using comparison and logical operators](#question-15---python-code-using-comparison-and-logical-operators)
  - [Question 16 - ACME Corporation - Coding Competency Application](#question-16---acme-corporation---coding-competency-application)
  - [**References**](#references)

## Question 1 - Web Development Markup Laguages

**Identify** and **explain** common and important components and concepts of web development markup languages   

- **tags**
  - Tags wrap the elements content. They signal how the content will be displayed as well as the beginning and end point for that particular element. (Erika Varagouli 2021) [^1]
- **Elements**
  - These are responsible for showing where an element begins and ends. (Erika Varagouli 2021) [^2]
- **Presentational Markup**
  - This type of markup is what is used in word processors and is nearly always hidden from the authors, editors and readers of the document. It uses binary codes embedded in documents to affect the text in a process coined WYSIWYG - What You See Is What You Get. (Wikipedia) [^3]
- **Procedural Markup**
  - With procedural markup, the instructions on how to process the text are embedded in the text itself. Markdown is a great example of this. The document's text is processed from top to bottom and when encountered, the procedural markup is applied to the text it is associated with. (Wikipedia) [^4]
- **Descriptive Markup / Semantic Markup**
  - This type of markup is used to convey the type of content that is being wrapped by a tag. It helps to convey the purpose of the text being presented.(Erika Varagouli 2021) [^5] Its purpose is to label parts of a document based on what the content is rather than how that content should be presented. (Wikipedia) [^6]

## Question 2 - Internet Technologies: Packets, IP, Routers and DNS

**Define** the features of the following technologies that are essential in terms of the development of the internet:
- **Packets**
  - A packet is the name given to the container that is used to send information around a packet-switched network. It contains two types of information, control information and user data.(Wikipedia) [^7]
- **IP addresses (IPv4 and IPv6)**
  - An IP (Internet-Protocol)  address is a unique address that is assigned to any computer or device that is connected to a network. The address is made up of 4 numbers connected (or separated) but full stops. e.g: 142.250.76.100 (MDN) [^8]
- **Routers and Routing**
  - Routers are responsible for getting a data packet to its intended destination.Data packets contain the destination IP address amongst other control information. Routing is the process of routers choosing the most efficient path for the data packet to travel on from source to destination.(cisco) [^9]
- **Domains and DNS**
  - IP addresses can be easily processed by a computer however they are quite difficult to remember for humans. The domain name is a name given to a web server that is connected to the internet. It is essentially an alias for the underlying IP address used to locate that particular web server. DNS stands for Domain Name System. DNS is similar to a registry or database where a web server's IP address is linked to its domain name. (Mozilla) [^10]

**Explain** how each technology has contributed to the development of the internet.
- **Packets**
  - Packets contributed to the development of the internet by allowing larger chunks of data to be broken up at the server and sent in smaller packets to the user or client. This meant that multiple clients/users could be downloading data from a single website at the same time. This would not be possible if the website had to be downloaded in one large chunk. Having data in small packets rather than large files also makes it easier and more efficient to resend data that is corrupted or lost.(Mozilla) [^11]
- **IP addresses (IPv4 and IPv6)**
  - Without IP addresses the internet wouldn't exist! Every device, whether it's a phone, tablet, PC or web server is assigned an IP address so that it can be located on the internet and is able to send and receive data to other devices. It may be allocated an IP address using either IP4, which uses 32bits for its address and IP6 which uses 128bits.(Wikipedia) [^12]
- **Routers and Routing**
  - Routers are an intermediary and create a network between the sender and the receiver. They will receive data from computer A and know which path to send that data so that it reaches its destination at computer B and not at computer C or D. Routers can also link to other routers and this fact allowed for the massive expansion of the internet. Creating a network of networks allows for a theoretical infinite amount of connections between devices on the internet.(Mozilla) [^13]
- **Domains and DNS**
  - With an ever increasing number of web servers on the internet, domains and DNS allowed users to access websites with easy to remember groups of words rather than random numbers separated by full stops. This is facilitated by a type of server called a  DNS server. This is a server that will translate the human readable domain name that is entered by the user into its associated computer readable IP address and will direct the user to the correct web server. Amazon) [^14]

## Question 3  - Internet Technologies: TCP, HTTP/HTTPS and Web Browsers

Define the features of the following technologies that are essential in terms of the development of the internet:
- **TCP**
  - The Transmission Control Protocol facilitates the connection between two hosts to allow the guaranteed transmission of data and packets in the correct order to the receiver. (Mozilla) [^15] Its main features are connection control, reliability, flow control and congestion control.(Noction) [^16]
- **HTTP and HTTPS**
  - The main features of the Hypertext Transfer Protocol are the client and the server. Requests for information are sent by the client, normally a web browser, to the server. The server then answers the request by sending back information to the client. This is called a response. The client (almost) always is the side sending the request. And the server will then serve the document requested as a response to the client.(Mozilla) [^17]
Hypertext Transfer Protocol Secure (HTTPS) is the same as HTTP except that it has more security that is provided by an SSL certificate and the SSL protocol. SSL stands for Secure Sockets Layer. (Javatpoint) [^18]
- **Web Browsers (requests, rendering and developer tools)**
  - A web browser is a piece of software that is used to view or access data on the internet. It sends requests to web servers for data and then once it gets a response and retrieves the data it will render that as a webpage on the user's device. (Wikipedia) [^19]
Developer tools are software add-ons that are included with a browser to allow web developers to inspect, test and debug their code. They work with a few different web technologies including HTML, CSS and JavaScript. (Wikipedia) [^20]

**Explain** how each technology has contributed to the development of client and server communication over the internet *(50 - 150 words for each technology)*.
- **TCP**
  - TCP’s ethos on accuracy over timeliness is one of the reasons it has contributed to the development of client-server communication over the internet. TCP can handle the extended delays in the delivery of packets that are out of order. This could occur if some packets take a different route to their destination or when corrupted packets need to be retransmitted. If timeliness is more important than accuracy then TCP is not the ideal protocol. For applications, like VOIP, that prioritise timeliness over accuracy, then other protocols such as RTP(Real-time transport Protocol) or UDP (User Datagram Protocol) may be better suited.
  - TCP guarantees that the data received at the client is exactly the data sent from the server. It achieves this accuracy using a technique called ‘positive acknowledgement with retransmission’ This technique involves the receiver sending an acknowledgement to the sender once the packet is received. The sender keeps a log of when a packet is sent and a timer from when the packet was sent. If a certain amount of time elapses and the sender has not received an acknowledgment yet, it will resend the packet. (Wikipedia) [^21]

- **HTTP and HTTPS**
  - These technologies have hugley contributed to client-server communication because they allow all the devices connected to the network to communicate with each other while not having a permanent connection between the client and the server. The network would be very limited in its size if every device needed a permanent connection to every other device for communication.
  When a connection is needed the client sends a request and the server ‘hears’ the incoming request and the connection is established. The server then waits for the message from the sender. The server's response includes the requested information. The connection can be closed at any time by either the client or the server. (Wikipedia) [^22]

- **Web Browsers (requests, rendering and developer tools)**
  - Web browsers play a vital part in client server communication. They represent the part of the ‘client’ in client-server communication. Client-server networking is an architecture where information is kept in a central location on servers and is shared with many clients in many different locations. The web browsers part as the client in this architecture is to send the requests for information to the server and accept the responses.
  - The centralised storage of data on servers allowed numerous clients, or web browsers, to access that data at the same time. In addition to receiving the raw information, the browser also renders that information into a webpage that can be easily viewed on a device. (LifeWire) [^23]
  - Browsers also have addons called developer tools. These have increased developers productivity by allowing them to directly view a website and edit the code locally to see immediately what changes would result from changing the code whether that be the CSS, HTML or JavaScript. Some other tools that assist developers are the ability to access web-page assets and network usage information such as the bandwidth used to load a page and what headers are being sent and received by the browser. JavaScript debugging within a developer tool suite is also commonly used. (Wikipedia) [^24]



## Question 4 - Python Data Structures

**Identify** THREE data structures used in the Python programming language and **explain** the reasons for using each.

- **Dictionary**
  - Python dictionaries are collections of data that are stored with key/value pairs where the key is immutable (does not change) and the value is mutable (can be changed). This structure makes it useful for the following reasons:
    - If the data that needs to be stored has a unique reference for the key. An example might be a membership ID, telephone number or email address
    - If the order that the data is stored is not important
    - When timeliness is crucial in relation to accessing a particular element. Dictionaries are designed to allow fast access to particular data based on the unique key because it means the whole database does not need to be scanned to find the right element. (Erdem Isbilen) [^25]  (RealPython) [^26] 
- **List**
  - Python lists are implemented as mutable dynamic arrays. This means that Python lists allow elements to be added, removed. They can store any type of object in python. This makes them highly versatile and the most commonly used data structure in Python and are used for many reasons such as the ones below.
    - When a developer needs to store a collection of data that is heterogenous, that is to say when all the data types are different. Python lists can store simple data structures like integers or strings alongside more complex structures like tuples, dictionaries or other lists!
    - When the order of the data is important. The order the data is entered into the list is preserved in a list. (Erdem Isbilen) [^27] (RealPython) [^28]
- **Set**
  - Python sets are a data structure similar to a dictionary and a list but has its own unique features. A set is an unordered list of entries. However, unlike a list, a set cannot have duplicate entries and each entry needs to be hashable, that is its value does not change over time. It has a few use cases listed below:
    - Checking a set for a value is very fast compared to a list. So if you're looking to store unordered, unique items that have a value that won't change then a set is preferable over a list.
    - They are useful for removing duplicates from a series of values
    - Sets support mathematical operations being performed on their data. These include intersection, union, difference and symmetric difference. (Python.org) [^29] (Stack overflow) [^30]

## Question 5 - Interpreters and Compilers

**Describe** the features of *interpreters* and *compilers* and how they are different.

Interpreters and compilers both translate higher level programming languages, or source code, into machine code made up of 0’s and 1’s. Although they have similar features they both use different processes to convert human readable source code into machine readable code.
A compiler will scan the whole program before it translates the source code, as a whole, into machine code. The analysis stage is much longer in duration than that of an interpreter but the overall execution time is faster than interpreters. Compilers require more memory because they create Object Code which requires linking. Common languages that use compilers are C, C++ and Java.
An interpreter will translate a program line by line and will take less time to analyse the source code compared to a compiler. However, it will take more time overal to execute the process. It wont produce any Object Code, so has no need for linking like a compiler, so is more efficient with its memory use. Examples of languages that use interpreters are Python, JavaScript and Ruby. (Programiz) [^31]

## Question 6 - Pros / Cons of Python and JavaScript

**Identify** TWO commonly used programming languages and **explain** the benefits and drawbacks of each.

- **Python - Benefits**
  - Extensive Libraries
    - Python’s standard library is extensive and comes packed with useful code and functions for regular expressions, documentation-generation, unit-testing, databases, image manipulation and more.
  - Extensible and embeddable
    - Python can be extended to other languages. You can write some of your code, for example, in C or C++.  Complementary to its extensibility, it is also embeddable. This means that python code can be embedded into the source code of other projects, for example, into C++.
  - Improved productivity
    - Python’s extensive libraries give developers access to pre-written functionality that allows them to solve common problems with a few lines of code. This allows more time to be spent on bigger picture problem solving.
  - Ease of use and readability
    - Python’s syntax is less complicated than other languages and it reads much like english, this makes it relatively easy to learn and use.
  - Free and Open-Source
    - Not only is Python free to download and use, but its source code is also available to download, change and distribute.
  - Portable
    - With software written in C or C++ changes may need to be made to make the software run on different platforms. This is not the case with Python as it uses a philosophy called Write Once Run Anywhere(WORA). However developers need to take caution to not use features that are system specific.
  - Interpreted rather than compiled
    - Python’s code is analysed line by line rather than as a whole, which happens in compiled languages. This makes debugging code easier than in compiled languages.
  - Object-Oriented
    - Python supports Object-oriented in addition to procedural programming philosophies. Python's functions help with code reusability. Objects and classes allow developers to model the real world. A class allows developers to combine and encapsulate functions and data.
  
- **Python - Drawbacks**
  - Speed limitations
    - Because python is interpreted rather than compiled, it executes the code line by line. This can result in slow execution of applications.
  - Weak adoption in mobile computing and browsers
    - Python is popular with server side applications however it is rarely seen used on client side applications because no major web browsers have python built into them. Although python has a framework called Django that can make its interactions with client side applications more streamlined.
  - Underdeveloped Database Access Layers
    - Python's Database Access Layers are fairly undeveloped compared to common technologies like JDBC (Java DataBase Connectivity) and ODBC (Open DataBase Connectivity). This means it has been less readily adopted for larger enterprise projects.
  - Design Restrictions - Dynamic Typing
    - Python is a Dynamically typed language which means that variables are allowed to change over their lifetime and that the interpreter only performs type checking when the code runs. While this is easier and more efficient for the developer when coding it can cause run time issues if the variable types are incorrect. (Data-flair) [^32] (Real Python) [^33]

- **JavaScript - Benefits**
  - Speed
    - As long as no other outside resources are needed, JavaScript runs immediately within the client's browser which makes it very fast to run code. JavaScript also isn't slowed down by calls to a server. All major browsers support Just In Time (JIT) compilation for JavaScript. JIT compilation means the code can be run without it being compiled first.
  - Simplicity
    - JavaScripts syntax is easy to learn and easier to read than other languages like C++
  - Popularity
    - JavaScript is ubiquitous on the web. Its is now available  and becoming more popular as a language to develop applications on servers with the release of Node.js. There is an abundance of projects on Github and StackOverflow that are written in JAvaScript and its popularity is only expected to increase.
  - Reduces Server Loads
    - Because javascript is mainly a client side language it greatly reduces the load on servers. There are some cases with smaller applications where a server is not needed at all
  - Creation of rich interface
    - JavaScript has the ability to create a host of features that contribute to webpage useability including drag and drop components and sliders that increase the quality of a user’s experience.
  - Versatility
    - JavaScript, through the use of frameworks and complementary technologies, becomes very versatile. It's possible to create an entire full-stack application with JavaScript. An example of this would be using a Node.js server, bootstrapping Express to Node.js and using MongoDB for a database. In addition to those backend technologies, using JavaScript for the frontend would mean the entire application was created with JavaScript
    - 
- **JavaScript - Drawbacks**
  - Browser interpretations
    - Server side scripts will always produce the same result. Different browsers, however, will occasionally interpret JavaScript code differently. These differences aren't huge so problems can be mitigated by testing the application across all the major browsers.
  - Client-side Security
    - Oversights in Javascript code can potentially be exploited by malicious actors because the code is executed within the browser. Because of this design flaw and potential security risk, a lot of people will completely disable JavaScript in their browser. (FreeCodeCamp) [^34]



## Question 7 - Ethics and Tech

**Identify** TWO ethical issues from the areas below and discuss the extent to which an IT professional is ethically responsible in terms of the issue.

List of topics containing ethical issues:
- access to a user’s personal information (medical, family, financial, personal attributes such as sexuality, religion, or beliefs)
- criminal acts such as theft, fraud, trafficking and distribution of prohibited substances, terrorism
- GPS tracking data and other types of metadata, MAC addresses, hardware fingerprints
- freedom of thought, conscience, speech and the media
- aggressive sales and marketing practices designed to mislead and deceive consumers
- trading of shares on the stock exchange OR crypto-currencies

For each ethical issue identify a source of legal information relating to the ethical issue and discuss whether the law is helpful in assisting a developer to act in an ethical way. *(Word count guide: 200 words max)*

Conduct **research** into a case study of **ONE** of the ethical issues you have chosen **discuss** how an ethical IT professional should respond to the case study and how they might mitigate or prevent ethical breaches. *(Word count guide: 400 - 600 words)*

## Question 8 - Control Flow in Python

Explain control flow, using examples from the Python programming language

## Question 9 - Type Coercion and Type Conversion in Python

Explain the difference between type coercion and type conversion. Are either of these used in Python?

## Question 10 - Data Types

Explain data types, using examples

## Question 11 - Classes

Here’s the problem: “There is a restaurant serving a variety of food. The customers want to be able to buy food of their choice. All the staff just quit, how can you build an app to replace them?”
- Identify the classes you would use to solve the problem
- Write a short explanation of why you would use the classes you have identified

## Question 12 - Find the error in a Code Snippet

Identify and explain the error in the code snippet below that is preventing correct execution of the program

<br>

<img src="./docs/workbook-q-12.png" width="600" alt="Q-12 Code Snippet">

<br>

This code results in a TypeError.


In this code, on line 2, the input() function will return a string and assign it to the celsius variable. The error is occurring on line 3 where there is a math calculation being attempted on two data types that are unsupported - between a string and a number.


## Question 13 - Rewrite a Code Snippet to swap two adjacent elements in an list

The code snippet below looks for the first two elements that are out of order and swaps them; however, it is not producing the correct results. Rewrite the code so that it works correctly.

<br>

<img src="./docs/workbook-q-13.png" width="600" alt="Q-13 Code Snippet">

<br>

```py
# creating the list of numbers
arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# printing the list of numbers
print("Original list\t", arr)

# Setting i to the value of 0 - the first element of the list
# iterating over the elments in the list while the i is less than the length of the list - 1 (zero index)
# and the while the current element's value is less than the next element's value.
i = 0
while ( i < len(arr) - 1) and (arr[i] < arr[i + 1]):
    # while true increment i
    i +=1
# I've left this in but all it does it print out the last index that is reached befre the while loop fails
print(i)

# Swap the current element with the next element
arr[i], arr[i + 1] = arr[i + 1], arr[i]

# printing the new list with the first two elements that are out of order now put in order
print("New list\t", arr)
```

**Output**

```
Original list    [5, 22, 29, 39, 19, 51, 78, 96, 84]
3
New list         [5, 22, 29, 19, 39, 51, 78, 96, 84]
```


## Question 14 - Algorithmic Thinking

Demonstrate your algorithmic thinking through completing the following two tasks, in order:
1. Create a flowchart to outline the steps for listing all prime numbers between 1 and 100 (inclusive). Your flowchart should make use of standard conventions for flowcharts to indicate processes, tasks, actions, or operations
2. Write pseudocode for the process outlined in your flowchart

## Question 15 - Python code using comparison and logical operators

Write pseudocode OR Python code for the following problem:

*You have access to two variables: raining (boolean) and temperature (integer). If it’s raining and the temperature is less than 15 degrees, print to the screen “It’s wet and cold”, if it is less than 15 but not raining print “It’s not raining but cold”. If it’s greater than or equal to 15 but not raining print “It’s warm but not raining”, and otherwise tell them “It’s warm and raining”*.

```py
if raining and temperature < 15:
    print("\nIt's wet and cold")
elif not raining and temperature < 15:
    print("\nIt's not raining but cold")
elif not raining and temperature >= 15:
    print("\nIt's warm but not raining")
else:
    print("\nIt's warm and raining")
```

## Question 16 - ACME Corporation - Coding Competency Application

ACME Corporation are hiring a new junior developer, as part of their hiring criteria they've created a "coding skill score" based on the specific competencies they require for this role; the more important the skill is for ACME corp, the more points it contributes to the "coding skill score" The skills are weighted as follows:
- Python (1)
- Ruby (2)
- Bash (4)
- Git (8)
- HTML (16)
- TDD (32)
- CSS (64)
- JavaScript (128)

Write a program that allows a user to input their skills and then tells them :

 a) Their overall "coding skill score"


 b) Skills they may want to learn, and how much each one would improve their score


 ## **References**

- [^1 - Tags](#question-1---web-development-markup-laguages) - https://www.semrush.com/blog/markup-language/
- [^2 - Elements](#question-1---web-development-markup-laguages) - https://www.semrush.com/blog/markup-language/
- [^3 - Presentational Markup](#question-1---web-development-markup-laguages) - https://en.wikipedia.org/wiki/Markup_language
- [^4 - Procedural Markup](#question-1---web-development-markup-laguages) - https://en.wikipedia.org/wiki/Markup_language
- [^5 - Descriptive Markup / Semantic Markup](#question-1---web-development-markup-laguages) - https://www.semrush.com/blog/markup-language/
- [^6 - Descriptive Markup / Semantic Markup](#question-1---web-development-markup-laguages) - https://en.wikipedia.org/wiki/Markup_language
- [^7 - Packets](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://en.wikipedia.org/wiki/Network_packet
- [^8 - IP addresses (IPv4 and IPv6)](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work
- [^9 - Routers and Routing](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/what-is-a-router.html
- [^10 - Domains and DNS](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name 
- [^11 - Packets](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works#packets_explained
- [^12 - IP addresses (IPv4 and IPv6)](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://en.wikipedia.org/wiki/IP_address
- [^13 - Routers and Routing)](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work
- [^14 - Domains and DNS)](#question-2---internet-technologies-packets-ip-routers-and-dns) - https://aws.amazon.com/route53/what-is-dns/
- [^15 - TCP](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://developer.mozilla.org/en-US/docs/Glossary/TCP)
- [^16 - TCP](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://www.noction.com/blog/tcp-transmission-control-protocol-congestion-control#:~:text=The%20main%20TCP%20features%20are,for%20creating%20multiple%20virtual%20connections.
- [^17 - HTTP and HTTPS](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#basic_aspects_of_http
- [^18 - HTTP and HTTPS](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://www.javatpoint.com/http-vs-https
- [^19 - Web Browsers](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://en.wikipedia.org/wiki/Web_browser
- [^20 - Web Browsers](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://en.wikipedia.org/wiki/Web_development_tools
- [^21 - TCP](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Network_function
- [^22 - HTTP and HTTPS](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_and_response_messages_through_connections
- [^23 - Web Browsers](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://www.lifewire.com/web-browsers-and-web-servers-communicate-817764
- [^24 - Web Browsers](#question-3---internet-technologies-tcp-httphttps-and-web-browsers) - https://en.wikipedia.org/wiki/Web_development_tools
- [^25 Data Structures: Dictionary](#question-4---python-data-structures) - https://towardsdatascience.com/python-dictionaries-651acb069f94
- [^26 Data Structures: Dictionary](#question-4---python-data-structures) - https://realpython.com/python-data-structures/#dictionaries-maps-and-hash-tables
- [^27 Data Structures: List](#question-4---python-data-structures) - https://towardsdatascience.com/a-complete-guide-to-python-lists-6b592c8d5707
- [^28 Data Structures: List](#question-4---python-data-structures) - https://realpython.com/python-data-structures/#list-mutable-dynamic-arrays
- [^29 Data Structures: Set](#question-4---python-data-structures) - https://docs.python.org/3/tutorial/datastructures.html#sets
- [^30 Data Structures: Set](#question-4---python-data-structures) - https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
- [^31 Interpreters and Compilers](#question-5---interpreters-and-compilers) - https://www.programiz.com/article/difference-compiler-interpreter
- [^32 Python pros / cons](#question-6---pros--cons-of-python-and-javascript) - https://data-flair.training/blogs/advantages-and-disadvantages-of-python/
- [^33 Python pros / cons](#question-6---pros--cons-of-python-and-javascript) - https://realpython.com/lessons/dynamic-vs-static/
- [^34 JavaScript pros / cons](#question-6---pros--cons-of-python-and-javascript) - https://www.freecodecamp.org/news/the-advantages-and-disadvantages-of-javascript/
- 



 [Go to top of page](#coder-academy---assignment-t1a1---workbook-submitted-by-mario-lisbona)