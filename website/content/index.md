---
weight: 1
title: "Easy laptop automated imager"
type: docs
---

## Problem statement

Recent developments in the world have pushed a lot of people to do remote work,
and students/kids to use remote education systems. There's basically two groups of
people now - those who are equipped to do remote, and those who are not for some reason.

Let's focus on a 'new' mode of education for a moment.

During a recent local survey in Poland, teachers and parents in Warsaw alone have
estimated a need for 20k+ extra laptops to be available for their kids/students
in order for them to be studying at all! There's couple of problems that have been
identified:

- suddenly, number of laptops and tablets should equal number of kids in a household,
as kids need an IT equipment piece each to attend daily classes
- the cost of this equipment is not trivial, especially with breaking supply chains around,
the availability of this equipment may be limited very soon
- even if you grab a new/used piece of equipment, initial setup is hard/not trivial
- it's much harder to get local IT support now

While this all was already a problem in a pre-COVID-19 world, it has become a really
amplified when this virus stroke us.

In short: people are missing properly setup, cheap gear to continue their education.

## The project

So, I have an idea to automate setting up laptops remotely for anyone that have any
good x86 piece of gear around. I want to make it possible for everyone to grab a cheap
laptop (used, post-leased, or just laying around with broken OS), and give them an option
to image and automatically set it up with all necessary components to run MS Teams,
Google classroom etc.

A common denominator for most remote work, classroom software and online documents systems is as follows:

- fairly recent web browser version

We can achieve that for literally free by installing any Linux.

## The plan

In order to do this, I've imagined following components needed:

- build a USB stick image to boot the initial installer from
- spawn a customised https://netboot.xyz/ instance on the public internet
- write a piece of PXE end-to-end automatic installer for Linux Mint
- write a simple PDF manual on how to image your own laptop
- create a website (Hugo powered?) that describes the idea and the whole process

## End result

Basically, you should be able to grab and 200-300$ post leased laptop, or the one that you
have already sitting on a shelf, and install a full OS with needed browsers using a USB stick
and an internet connection - without really touching or setting anything up yourself!

## How do I test this?

It's fairly easy, follow these steps please:

- Go to our relases page here: https://github.com/sokoow/globalhack-laptop-installer/releases
- From the latest release, section Assets, download a file called ```boot.zip```
- Unzip this file, you will get a ```boot.iso``` file as a result of this step
- Your ```boot.iso``` file is ready to be booted from CD, if you're into it
- In order to boot from the USB, you need to download Etcher: https://www.balena.io/etcher/ . It's a tool to convert your iso file into a bootable USB key (USB pendrive required here).
- Now the tricky part: you need to connect the laptop you'll be imaging to your wireless router with an Ethernet cable. Making this system work through WiFi is very hard (impossible at the moment), so you'll need to connect a cable to your laptop.
- Once your laptop is ready and connected to your router, boot from CD or USB. In most laptops you need to press F10 or F12 when you turn it on, and select CD or USB boot.
- You will see a small blue menu, choose your Ubuntu language there. 
**WARNING: This will erase your laptop's hard drive and install a brand new OS, make sure you want that**
- After you've chosen your Ubuntu language flavor, the process is fully automatic. Stay patient, a lot of messages go through the screen. It may get especially stuck at a customization part (step will contain "Preseed" text)
- Wait, probably like an hour
- Wait till your machine reboots itself.
- Remove your USB key, you should get a logon prompt. Username is ```student``` password ```student```
- Setup your Wifi (upper right corner of the screen). Enjoy your web browsers!

## Staff needed

In order to complete this, we'll need following profiles of people:

- technical writer/marketing (PDF manual + site contents)
- someone that knows Jekyll/Hugo to create a simple static website
- another SRE/DevOPS - to help me testing/spawning the environments
- testers with their own cheap/spare laptops

Have a look at our issues list in order to help: https://github.com/sokoow/globalhack-laptop-installer/issues

## FAQ

### What are hardware requirements here?

- theoretically it should work with any Desktop or Laptop
- it only works on x86 64bit machines (Intel and AMD based laptops and desktops)
- you should have a minimum of 4GB of memory, 12GB of hard drive space
- fairly quick internet connection (10Mbps+ recommended)

### What if it doesn't work on my machine?

Well, tough, try another one - we don't have any time for support here, but are trying to make the whole process work most of the time.

### Where are any PDF manuals?

They're being written as you read it, in many languages.

### Where's the source code?

It's being cleaned up, once posted, we'll post references and thanks to all projects that were used to build it.

### Why Ubuntu and Mint?

First reason is that it's very easy to automate these two end to end (well, not that easy on Mint, but easy enough). Second is that they have publicly accessible mirrors that will handle this experiment in a larger scale, and not a bad documentation and community.

### Can this install Windows or Mac OSX ?

If you find an easy legal way of automating that part over the internet, feel free to contribute and open up a pull request.

### Can I have a linux distribution X installed through this ?

Yes, if you help automating it, we'll plug it in (PRs welcome). We've linked ```netboot.xyz``` as a last menu option, so you can experiment with a lot of other distros in livecd mode.

### What about Chromebooks and ARM ?

Well, didn't try that yet...

## Thanks so far

- Authors of https://github.com/netbootxyz/netboot.xyz - your system is really an inspiration for all this. good work.
- Authors of https://github.com/acefei/ace-osinstaller - you've really helped with automating a lot with this. Big kudos.
- @jozwior - for parts of Ubuntu seed code that just worked out of the box.

Join us!
