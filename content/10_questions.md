Title: 10 best questions about public cloud
Tags: Cloud, DevOps

Some time ago, I invited a bunch of smart folks in the [Linux Expert](https://www.linkedin.com/groups?home=&gid=49301) LinkedIn group to ask me questions about public clouds.

I want to share 10 of these questions with you (there were many more!). I think that these are the most important for any cloud beginner – and of course, I’ll provide you with my answers.

##1. Why should I use the cloud?

You should use the cloud because its Return-on-Investment (ROI) is generally better than the alternatives (e. g. investing in your own hardware and datacenter management).

In some special cases, building and managing your own infrastructure (private cloud) is cheaper.

In other cases, local regulations preclude you from using a public cloud.

##2. What existed before the cloud?

The current generation of public cloud providers began with the Amazon Web Service (AWS), which introduced its first cloud offering in 2006.
Before that, the closest we had to public clouds were the various hosting providers.
For example, although you could order servers and possibly storage from such providers – the provisioning time was measured in weeks.
In addition, you typically had to agree to a long term contract.

However, if you go deeper into the history of computing, it turns out that public cloud is not a new idea!
For instance, consider the Multics operating system (one of the precursors of Unix).
It was designed in 1964 as a computing utility, modeled on the electrical or telephone utilities.
See [Time Sharing](http://en.wikipedia.org/wiki/Time-sharing) and [Cloud Computing](http://en.wikipedia.org/wiki/Cloud_computing) Wikipedia articles for further reference.

##3. Do cloud providers guarantee that my cloud will be 100% secure? If not, to what level will it be secure?

No, they don't. However, they do support various industry standards and regulations like [PCI DSS](https://www.pcisecuritystandards.org/security_standards/), [HIPAA](http://health.state.tn.us/hipaa/), and [ISO 27001](http://www.iso.org/iso/home/standards/management-standards/iso27001.htm).

In general, the level of security from a public cloud's provider will be definitely higher than what you can achieve on your own.

##4. What (Open Source preferred) software is needed to join the cloud? – And by 'joining the cloud' I don't mean 'using', but participating - like when you join the Internet, where there is no distinction between provider and consumer.

Wow! You’re proposing  a really cool thing: something like a peer-to-peer cloud!
Theoretically, you could build it, but none of the current big providers work like that.
There is such a thing as a peer-to-peer cloud storage, but it is very early in its development stage - check this [startup.](http://storj.io/)

Also, for an in-depth overview, read this [article](http://spectrum.ieee.org/computing/networks/escape-from-the-data-center-the-promise-of-peertopeer-cloud-computing).

##5. Is the cloud subject to any national legislation or law enforcement issues?

Yes and no. YES, because there are current laws governing data locality, which is a big part of the issue, and NO because there are no new laws (that I know of) that cover complicated cloud use scenarios.
See this [article](http://www.wsj.com/articles/michael-chertoff-wanted-an-international-rule-of-law-to-govern-the-cloud-1418946310) for a good summary.

##6. Can I have Private cloud and public cloud, and sync between them?

Yes, you can make your software run on something like the [OpenStack](https://www.openstack.org/) installation, together with [AWS](https://aws.amazon.com/), and use the same API to move data between the two installations.
Your software doesn’t really care if it’s currently talking with AWS or OpenStack.
Just change the endpoint name (where to connect), but the commands stay the same.

##7. What is the best way for beginners to start learning (for example: via private cloud and then moving to public cloud)?

Actually, the best way is just the opposite. Begin with a public cloud and then move to a private one.
The reason is very simple: the public cloud is already there, you don't have to set anything up.

The whole point of using the cloud is to be as independent and free as possible, and not have to bother with setting anything up, etc.


##8. What is the difference between Shared hosting, VPS, Dedicated hosting, and Cloud Hosting?
In shared hosting, you get a slice of resources on a server (for example: 10 GB of disk space). There is typically no virtualization.  
Under VPS you have a virtualized server. It runs on the same hardware with other virtualized servers, and you order it from a hosting provider.  
Dedicated hosting requires buying a hardware server to which you have bare metal access. You pay for its electricity bill, air conditioning, and Internet connectivity.  
Finally, the Public cloud offers a virtualized server similar to VPS, but you get access to it using self-service APIs.

##9. What is the role of System Admin when 100% of the servers are hosted in the public cloud ?

Don’t worry – they’ll be busy enough ☺.  
For example, working with APIs that provision and configure servers and networks.  
Which is basically continuing to do the same work, but at a different level of abstraction.  
Also take a look at the [DevOps](http://en.wikipedia.org/wiki/DevOps) role.

##10. What type of technology stack will drive the Cloud computing: closed or open?

This area is complicated and changes continuously.
For now, the dominant player in public cloud is [AWS](https://aws.amazon.com/) and their stack is closed.
On the other hand you have [OpenStack](https://www.openstack.org/), used primarily for private clouds.
To further complicate matters, we have all the buzz from [Docker](https://www.docker.com/) and its [ecosystem](https://www.docker.com/partners/find/) - which is mostly open.

And here’s a bonus question:
##How does an application "developed for the cloud" differ from a "normal" application?

I LOVE this question!  
First, understand that the difference between "datacenter" app architecture and "cloud" app architecture is one of the most crucial factors in using the cloud successfully.  

And what is that difference?  
In short, the datacenter apps are optimistic with regard to infrastructure, while cloud apps are realistic.  
Cloud apps are typically deployed on multiple virtual machines, where a loss of a single machine does not affect the application, while the datacenter apps are much more finicky about the failures of underlying hardware.
In addition, the datacenter environment is static, while the cloud is dynamic.
This necessitates adding service discovery mechanisms, but as a result, this makes the app even more robust.
Last but not least, most of the datacenter applications are monolithic, while [microservices](http://martinfowler.com/articles/microservices.html) are a hot topic in today's cloud conversations.
