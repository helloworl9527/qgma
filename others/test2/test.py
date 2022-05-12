import os
class Platform:
	def __init__(self):
		self.plugins=[]
		self.loadPlugins()

	def sayHello(self, from_):
		print("hello from %s.") % from_

	def loadPlugins(self):
		print("********** loadPlugins **********")
		print("listdir(plugins): "), os.listdir("plugins")
		for filename in os.listdir("plugins"):
			if not filename.endswith(".py") or filename.startswith("_"):
				continue
			self.runPlugin(filename)

	def runPlugin(self, filename):
		print("********** runPlugin **********")
		pluginName=os.path.splitext(filename)[0]
		print('pluginName: '), pluginName
		plugin=__import__("plugins."+pluginName, fromlist=[pluginName])
		clazz=plugin.getPluginClass()
		o=clazz()
		print('clazz: '), clazz
		o.start()
		self.plugins.append()

	def shutdown(self):
		for o in self.plugins:
			o.stop()
			o.setPlatfrom(None)
		self.plugins=[]

if __name__=="__main__":
	platform=Platform()
	platform.shutdown()
