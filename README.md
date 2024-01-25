# Registry Factory

## About the project
The project started out as a backend for Kroozheva web application which was meant to be 
a graph based tool for linking different entities and quickly finding relations between 
them. 

For example, we could start out creating a person, a company and a city as separate nodes. We could then
link them such that it was clear that the person and the company are in the same city and the 
person is an employee of the company. 

People, companies and cities are only examples. Entities could be anything you could think of.
For example, such a graph can be used to create relations of your home library, your business, etc.

The point of the application is finding links quickly without the need to make queries programmatically,
but rather search and filter within the user interface. Suppose you need a doctor in your area, 
and you'd like to see whether you have any connections that lead to doctors. You can type in "doctor" and
the application will fetch any doctors you have in your connections. From then on you can proceed
looking up their details, including exactly how you are connected. Maybe your sister is a doctor,
maybe your friend is married to a doctor, etc.

The real power of the idea becomes apparent when we imagine multiple users that share their connections
with each other. Now your network becomes much broader. You can find a link to what / who you are looking for,
and you know how you are connected exactly.

Here are a couple of screenshots of the application
![Kroozheva example 1](media/Kroozheva%20ex1.png)

![Kroozheva example 2](media/Kroozheva%20ex2.png)

![Kroozheva example 3](media/Kroozheva%20ex3.png)

## Development
During development, it became obvious that the entities are very similar except "links" entities.
Since we needed more and more of them, we created a template of an entity (I'm going to refer
to entities **registries** from now  on). 

Such a registry can be created by running a single command. Out of the box the registry comes with CRUD
API, automatic swagger UI and full set of regression tests.

So the project was now called **"Registry Factory"** and was utilized as the backend for 
many other projects within the company. In fact, it was the pioneer service as the company
started shifting towards the microservice architecture.

## Documentation
The documentation is available on Wiki. 
* [Registry creation guide](https://github.com/imikhassik/Registry-Factory/wiki/Registry-creation-guide)
* [Registry deployment instructions](https://github.com/imikhassik/Registry-Factory/wiki/Registry-API:-Deployment-Instructions)
* [API documentation](https://github.com/imikhassik/Registry-Factory/wiki/Registry-API:-Documentation-v-0.4.3)
* [Adding a registry to existing registries guide](https://github.com/imikhassik/Registry-Factory/wiki/Registry-API:-Adding-New-Registry-Instructions)
* [Release notes](https://github.com/imikhassik/Registry-Factory/wiki/Registry-API:-Release-Notes)
