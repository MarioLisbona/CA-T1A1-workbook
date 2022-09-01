# **Coder Academy - Assignment T1A1 - Workbook: Submitted by Mario Lisbona**

## **Table of contents**

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

## Question 4 - Python Data Structures

**Identify** THREE data structures used in the Python programming language and **explain** the reasons for using each.

## Question 5 - Interpreters and Compilers

**Describe** the features of *interpreters* and *compilers* and how they are different.

## Question 6 - Pros / Cons of Python and JavaScript

**Identify** TWO commonly used programming languages and **explain** the benefits and drawbacks of each.

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

## Question 13 - Rewrite a Code Snippet to swap two adjacent elements in an list

The code snippet below looks for the first two elements that are out of order and swaps them; however, it is not producing the correct results. Rewrite the code so that it works correctly.

<br>

<img src="./docs/workbook-q-13.png" width="600" alt="Q-13 Code Snippet">


## Question 14 - Algorithmic Thinking

Demonstrate your algorithmic thinking through completing the following two tasks, in order:
1. Create a flowchart to outline the steps for listing all prime numbers between 1 and 100 (inclusive). Your flowchart should make use of standard conventions for flowcharts to indicate processes, tasks, actions, or operations
2. Write pseudocode for the process outlined in your flowchart

## Question 15 - Python code using comparison and logical operators

Write pseudocode OR Python code for the following problem:

*You have access to two variables: raining (boolean) and temperature (integer). If it’s raining and the temperature is less than 15 degrees, print to the screen “It’s wet and cold”, if it is less than 15 but not raining print “It’s not raining but cold”. If it’s greater than or equal to 15 but not raining print “It’s warm but not raining”, and otherwise tell them “It’s warm and raining”*.

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



 [Go to top of page](#coder-academy---assignment-t1a1---workbook-submitted-by-mario-lisbona)