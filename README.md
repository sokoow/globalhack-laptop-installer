# Problem statement

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
- it's much harder to get local IT support

While this all was already a problem in a pre-COVID-19 world, it has become a really
amplified when this virus stroke us.

In short: people are missing properly setup, cheap gear to continue their education.

# The project

So, I have an idea to automate setting up laptops remotely for anyone that have any
good x86 piece of gear around. I want to make it possible for everyone to grab a cheap
laptop (used, post-leased, or just laying around with broken OS), and give them an option
to image and automatically set it up with all necessary components to run MS Teams,
Google classroom etc.


# The plan

In order to do this, I've imagined followin components needed:

- build a USB stick image to boot the initial installer from
- spawn a customised https://netboot.xyz/ instance on the public internet
- write a piece of PXE end-to-end automatic installer for Linux Mint
- write a simple PDF manual on how to image your own laptop
- create a simple website (Hugo powered?) that describes the idea and the whole process

# The end result

Basically, you should be able to grab and 200-300$ post leased laptop, or the one that you
have already sitting on a shelf, and install a full OS with needed browsers using a USB stick
and an internet connection - without really touching or setting anything up yourself!

# Staff needed
In order to complete this, we'll need following profiles of people:
- technical writer/marketing (PDF manual + site contents)
- someone that knows Jekyll/Hugo to create a simple static website
- another SRE/DevOPS - to help me testing/spawning the environments
- testers with their own cheap laptops

Join me! 
