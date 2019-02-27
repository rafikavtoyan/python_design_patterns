"""
One	of	the	use	cases	for	the	Singleton	pattern	is	lazy	instantiation.	For	example,	in	the
case	of	module	imports,	we	may	accidently	create	an	object	even	when	it’s	not	needed.
Lazy	instantiation	makes	sure	that	the	object	gets	created	when	it’s	actually	needed.
Consider	lazy	instantiation	as	the	way	to	work	with	reduced	resources	and	create	them
only	when	needed.
"""


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("	__init__ method called..")
        else:
            print("Instance already created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()  # class initialized, but object not created
print("Object created", Singleton.get_instance())  # Object gets created here
s1 = Singleton()  # instance already created
