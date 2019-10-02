import subprocess
import os
import time

class QueryExecutor:
	def __init__(self, ):
		### Always Runs in Quiet Mode
		### For information about logs, specify
		##  in the log file.

		## query instruction build
		## stores last query executed, this is also used in runQuery and callQuery
		self.query = ''

		## show in json format
		self.json = False

		## show in html format we can use only one format at a time
		self.html = False

		## number of processes
		self.processes = 1

		## directory for extracted files
		## default value as text (no flags needed for this)
		self.output = 'text'

		## maximum bytes per output file
		self.bytes = 1000000

		## output file compression using bzip
		self.compress = False

		## preserve links or not
		self.links = False

		## preserve section or not
		self.sections = False

		## preserve list or not
		self.lists = False

		## accepted namespaces in links comma separated
		self.namespaces = ''

		## use or create file containing templates
		self.templates = ''

		## do not expand templates
		self.do_not_expand_templates = False

		## Minimum expanded text length required to write document
		self.min_text_length = 0

		## Include or exclude specific categories from the dataset.
		self.path_of_category_file = ''

		## Remove pages from output that contain disabmiguation markup
		self.filter_disambig_pages = False

		## comma separated list of tags that will be dropped, keeping their content
		self.ignored_tags = ''

		## comma separated list of elements that will be removed from the article text
		self.discard_elements = ''

		## Preserve tables in the output article text
		self.keep_tables = False

		## will save log information in this file
		self.log_file = ''

		## generate file from this plain text by appending dummy tags
		## Because the wikiExtractor works only with those tags
		self.text = ''


	## sets OutputFile Directory Name (used in query building stage)
	def setOutputFileDirectoryName(self, outputDirectory = 'text'):
		self.output = outputDirectory

	## getter function for output file directory
	def getOutputFileDirectoryName(self):
		return self.output

	#setter function
	## flips json and html
	def setJson(self):
		self.json = True
		self.html = False

	#setter function
	## flips json and html
	def sethtml(self):
		self.html = True
		self.json = False


	#setter function
	def setNumberOfProcesses(self, numOfProcesses):
		self.processes = numOfProcesses

	## getter function
	def getNumberOfProcesses(self, numOfProcesses):
		return self.numOfProcesses

	#setter function
	def setNumberOfBytes(self, numOfBytes):
		self.bytes = numOfBytes

	## getter function
	def getNumberOfBytes(self):
		return self.bytes

	#setter function
	def setCompress(self, compressValue):
		self.compress = compressValue

	## getter function
	def getCompressValue(self):
		return self.compress

	#setter function
	def setPreserveLinks(self, preserveValue):
		self.links = preserveValue

	## getter function
	def getPreserveValue(self):
		return self.links

	#setter function
	def setPreserveSections(self, preserveValue):
		self.sections = preserveValue

	## getter function
	def getPreserveSections(self):
		return self.sections

	#setter function
	def setPreserveLists(self, preserveValue):
		self.lists = preserveValue

	## getter function
	def getPreserveLists(self):
		return self.lists

	#setter function
	def setNamespaces(self, ns_list_comma_Separated):
		self.namespaces = ns_list_comma_Separated

	## getter function
	def getNamespaces(self):
		return self.namespaces

	#setter function
	def setTemplates(self, template):
		self.templates = template

	## getter function
	def getTemplates(self):
		return self.templates

	#setter function
	def setMinTextLength(self, min_length):
		self.min_text_length = min_length

	## getter function
	def getMinTextLength(self):
		return self.min_text_length

	#setter function
	def setPathOfCategoryFile(self, file_path):
		self.path_of_category_file = file_path

	## getter function
	def getPathOfCategoryFile(self):
		return self.path_of_category_file

	#setter function
	def setDisambiguationPages(self, setValue):
		self.filter_disambig_pages = setValue

	## getter function
	def getDisambiguationPages(self):
		return self.filter_disambig_pages

	#setter function
	def setIgnoredTagsCommaSeparated(self, comma_separated_tags):
		self.ignored_tags  = comma_separated_tags

	## getter function
	def getIgnoredTagsCommaSeparated(self):
		return self.ignored_tags

	#setter function
	def setDiscardElementsCommaSeparated(self, comma_separated_elements):
		self.discard_elements = comma_separated_elements

	## getter function
	def getDiscardElementsCommaSeparated(self):
		return self.discard_elements

	#setter function
	def setKeepTables(self, keepValue):
		self.keep_tables = keepValue

	## getter function
	def getKeepTables(self):
		return self.keep_tables

	#setter function
	def setLogFileName(self, log_file_name):
		self.log_file = log_file_name

	## getter function
	def getLogFileName(self):
		return self.log_file

	#setter function
	def setDoNotExpandTemplates(self, do_not_expand_templates_value):
		self.do_not_expand_templates = do_not_expand_templates_value

	## getter function
	def getDoNotExpandTemplates(self):
		return self.do_not_expand_templates

	#setter function
	def setMinTextLength(self, min_text_length_value):
		self.min_text_length = min_text_length_value

	## getter function
	def getMinTextLength(self):
		return self.min_text_length

	## write in file method
	## intermediate method (you don't need to do it)
	def writeInFile(self, text_value):
		with open('input.xml', 'w') as file:
			file.write(text_value)

	## set text value
	## appends prefix and suffix to text and sets them to
	## the internal variable for further processing
	def setTextValue(self, text_value):

		prefix = """<page>
    <id></id>
    
      <text xml:space="preserve" bytes="1182"> """

		suffix = """</text>
     
  </page> """

		self.text = prefix + text_value + suffix
		self.writeInFile(self.text)


	## gives text value 
	def getTextValue(self):
		return self.text





	## querybuilder method
	## used to build query using presetted descriptors
	## Note: queries always run in --silent mode
	def buildQuery(self):
		cmd = 'python WikiExtractor.py input.xml '# --processes 4 --links --output lol --quiet'

		if(self.json):
			cmd += '--json '
		if(self.html):
			cmd += '--html '

		cmd += '--output ' + self.output + ' '

		cmd += '--processes ' + str(self.processes) + ' '

		if(self.bytes != 1000000):
			cmd += '--bytes ' + str(self.bytes) + ' '

		if(self.compress):
			cmd += '--compress '

		if(self.links):
			cmd += '--links '

		if(self.sections):
			cmd += '--sections '

		if(self.lists):
			cmd += '--lists '

		if(self.namespaces != ''):
			cmd += '--namespaces ' + str(self.namespaces) + ' '

		if(self.templates != ''):
			cmd += '--templates ' + str(self.templates) + ' '

		if(self.do_not_expand_templates):
			cmd += '--no-templates '

		if(self.path_of_category_file != ''):
			cmd += '--filter_category '

		if(self.filter_disambig_pages):
			cmd += '--filter_disambig_pages '

		if(self.ignored_tags != ''):
			cmd += '--ignored_tags ' + str(self.ignored_tags)

		if(self.discard_elements != ''):
			cmd += '--discard_elements ' + str(self.discard_elements) + ' '

		if(self.keep_tables):
			cmd += '--keep_tables '

		if(self.log_file != ''):
			cmd += '--log_file ' + str(self.log_file) + ' '


		cmd += '--quiet'

		self.query = cmd

		print(cmd)
		#os.system(cmd)

	## callquery method
	## uses system call to run the query command
	def callQuery(self):
		os.system(self.query)

	## queryrunner method
	## builds the query using query text and then runs it
	def runQuery(self):
		self.buildQuery()
		self.callQuery()

	## returns the result in pure text form
	## result is coming from file from self.output/AA/wiki_00 file
	## wiki_00 is generated using wikiExtractor
	def result(self):
		final_output = ''
		file_path = self.output + "/AA/wiki_00"
		with open(file_path) as file:
			final_output = file.read()
			return final_output


##############################################################################################

                                             ### Testing ###

input_text = """



{{Infobox tornado single
| name = July 2006 Westchester County tornado
| image location = 2006 Westchester Tornado California Closests.jpg
| image name =The California Closets Warehouse that was severely damaged by the tornado
| date = July 12, 2006
| time = 3:30 p.m. &amp;ndash; 4:03 p.m. [[Eastern Time Zone|EDT]]
| fujitascale = F2
| total damages (USD) = $12.1 million (2006 [[United States Dollar|USD]])&lt;br&gt; $12.9&amp;nbsp;million (2008 USD)
| total fatalities = None (6 injuries)
| area affected = [[Rockland County, New York|Rockland]] and [[Westchester County, New York|Westchester]], [[New York]]; and [[Fairfield County, Connecticut|Fairfield]], [[Connecticut]]
}}


The '''July 2006 Westchester County tornado''' was an [[Fujita_scale#Parameters|F2]] [[tornado]] that touched down in [[Rockland County, New York]] on July&amp;nbsp;12,&amp;nbsp;2006. It traveled {{convert|13|mi|km}} into southwestern [[Connecticut]] during a 33-minute span through two states. The tornado touched down at 3:30&amp;nbsp;p.m.&amp;nbsp;[[Eastern Time Zone|EDT]] (19:30&amp;nbsp;[[Coordinated Universal Time|UTC]]) on the shore of the [[Hudson River]] before becoming a [[waterspout]] and traveling {{convert|3|mi|km|abbr=on|sigfig=1}} across the river. Coming ashore, the tornado entered [[Westchester County, New York|Westchester County]] and struck the town of [[Sleepy Hollow, New York|Sleepy Hollow]] at F1 intensity. After passing through the town, it intensified into an F2 tornado and grew to almost a quarter mile (400&amp;nbsp;m) in diameter,&lt;ref name="MSSum"/&gt; making it both the strongest and largest tornado in the county's history.&lt;ref name="THPWest"/&gt; The tornado continued through the county, causing damage to numerous structures, until it crossed into Connecticut at 4:01&amp;nbsp;p.m.&amp;nbsp;EDT (20:01&amp;nbsp;UTC). Not long after entering the state, it dissipated near the town of [[Greenwich, Connecticut|Greenwich]] at 4:03&amp;nbsp;p.m.&amp;nbsp;EDT (20:03&amp;nbsp;UTC).&lt;ref name="MSSum"/&gt; When the tornado entered Westchester County, it was the eighth known tornado to either touch down or enter the county since 1950.&lt;ref name="THPWest"&gt;{{cite web| author=[[Storm Prediction Center]]| year=2007| title=Tornado History Project: Westchester, New York Tornadoes, 1950-2007| publisher=Joshua Lietz (TornadoHistoryProject.com)| accessdate=2008-12-06|url=http://tornadohistoryproject.com/tornado.php?yr=%25&amp;mo=%25&amp;day=%25&amp;st=New+York&amp;fu=%25&amp;co=Westchester&amp;l=auto&amp;submit=Table&amp;ddat=on&amp;dsta=on&amp;dfuj=on&amp;dfat=on&amp;dinj=on&amp;dcou=on&amp;format=basic&amp;p=1&amp;s=1}}&lt;/ref&gt;
The tornado left significant damage in its wake. Two barns and a warehouse were destroyed, and a large stained-glass window was shattered. Numerous homes and businesses were damaged and thousands of trees were uprooted. There were no fatalities and only six minor injuries were associated with the storm. Damages from the tornado totaled $12.1&amp;nbsp;million (2006 [[United States Dollar|USD]]; $12.9&amp;nbsp;million 2008 USD).

==Meteorological synopsis==
On July&amp;nbsp;12, a [[supercell]] [[thunderstorm]] developed over eastern [[New Jersey]] in association with a [[Low pressure area|surface low-pressure area]] in southwestern [[Ontario]]. Daytime heating in the [[Tri-State Region]] led to moderate instability, a key factor in the development of [[Atmospheric convection|showers and thunderstorms]]. With conditions favorable for the development of a [[tornado]], the [[Storm Prediction Center]] issued a [[tornado watch]] at 12:40&amp;nbsp;p.m.&amp;nbsp;[[Eastern Time Zone|EDT]] (16:40&amp;nbsp;[[Coordinated Universal Time|UTC]]).&lt;ref name="Tornadowatch"&gt;{{cite web| author=Thompson| date=2006-07-12| title=Severe Weather Watch #593 (Tornado Watch)| publisher=[[Storm Prediction Center]]| accessdate=2008-11-29|url=http://www.spc.noaa.gov/products/watch/2006/ww0593.html}}&lt;/ref&gt; A strong thunderstorm developed around 2:00&amp;nbsp;p.m.&amp;nbsp;EDT (18:00&amp;nbsp;UTC) which produced a [[funnel cloud]] near [[Carlstadt, New Jersey|Carlstadt]] at around 2:45&amp;nbsp;p.m.&amp;nbsp;EDT (18:45&amp;nbsp;UTC), although no damage was associated with the funnel.&lt;ref name="NJFunnel"&gt;{{cite web| author=Stuart Hinson| year=2006| title=July 12, Weather Event #625643 (Funnel Cloud)| publisher=[[National Climatic Data Center]]| accessdate=2008-11-29|url=http://www4.ncdc.noaa.gov/cgi-win/wwcgi.dll?wwevent~ShowEvent~625643}}&lt;/ref&gt; That same storm intensified and developed into a supercell as it crossed into [[New York]].&lt;ref name="Tornado1"/&gt; About 15&amp;nbsp;minutes later, a [[tornado warning]] was issued for southern Rockland and [[Westchester County, New York|Westchester]] counties which would remain in effect until 4:15&amp;nbsp;p.m.&amp;nbsp;EDT (21:15&amp;nbsp;UTC).&lt;ref name="WCBS"/&gt; At around 3:30&amp;nbsp;p.m.&amp;nbsp;EDT (19:30&amp;nbsp;UTC), an [[Fujita_scale#Parameters|F1]] tornado touched down near [[Grand View-on-Hudson, New York|Grand View-on-Hudson]] along the [[Hudson River]] in [[Rockland County, New York|Rockland County]]. The 100&amp;nbsp;yard (91&amp;nbsp;m) wide tornado touched down on a dock before becoming a [[waterspout]] as it took a {{convert|3|mi|km|abbr=on}} path across the river. The tornado passed near the [[Tappan Zee Bridge]] before crossing into [[Westchester County, New York|Westchester County]].&lt;ref name="Tornado1"&gt;{{cite web| author=Stuart Hinson| year=2006| title=July 12, Weather Event #626587 (Tornado)| publisher=[[National Climatic Data Center]]| accessdate=2008-11-29|url=http://www4.ncdc.noaa.gov/cgi-win/wwcgi.dll?wwevent~ShowEvent~626587}}&lt;/ref&gt; Upon entering Westchester, it was the eighth tornado ever recorded in the county.&lt;ref name="THPWest"/&gt;

The tornado hit the town of [[Sleepy Hollow, New York|Sleepy Hollow, New York]] around 3:37&amp;nbsp;p.m.&amp;nbsp;EDT (19:37&amp;nbsp;UTC); two minutes later, a {{convert|58|mph|km/h|abbr=on}} wind gust was reported along the periphery of the tornado. As the tornado neared [[New York State Route 9A]], it intensified to F2 status, generating winds up to {{convert|157|mph|km/h|abbr=on}}, and struck the California Closet Warehouse. At the time, the tornado was estimated to be 300&amp;nbsp;yd (274&amp;nbsp;m) wide&lt;ref name="Tornado2"/&gt; and was the strongest tornado ever recorded in Westchester County.&lt;ref name="USAT"&gt;{{cite news| author=Jim Fitzgerald| date=2006-07-14| title=Weather Service confirms F-2 tornado roared through N.Y., Conn. on Wednesday| work=[[USA Today]]| accessdate=2008-11-29|url=http://www.usatoday.com/weather/storms/2006-07-14-ny-tornado-confirmed_x.htm}}&lt;/ref&gt; Shortly after, it weakened back to F1 intensity. Minor damage was reported through the [[Kensico Reservoir]] in [[Valhalla, New York|Valhalla]] as the tornado neared the New York&amp;ndash;[[Connecticut]] border. The track length through Westchester County was measured at around {{convert|8|mi|km|abbr=on}}.&lt;ref name="Tornado2"&gt;{{cite web| author=Stuart Hinson| year=2006| title=July 12, Weather Event #626588 (Tornado)| publisher=[[National Climatic Data Center]]| accessdate=2008-11-29|url=http://www4.ncdc.noaa.gov/cgi-win/wwcgi.dll?wwevent~ShowEvent~626588}}&lt;/ref&gt; After crossing the state border into [[Fairfield County, Connecticut]], it weakened further before lifting at 4:03&amp;nbsp;p.m&amp;nbsp; EDT (20:03 UTC) in [[Greenwich, Connecticut|Greenwich]] after traveling {{convert|2|mi|km|abbr=on}} in Connecticut. Another brief touchdown may have occurred shortly after near the [[Merritt Parkway]].&lt;ref name="Tornado3"&gt;{{cite web| author=Stuart Hinson| year=2006| title=July 12, Weather Event #606978 (Tornado)| publisher=[[National Climatic Data Center]]| accessdate=2008-11-29|url=http://www4.ncdc.noaa.gov/cgi-win/wwcgi.dll?wwevent~ShowEvent~606978}}&lt;/ref&gt; Overall, the tornado tracked across a total of {{convert|13|mi|km|abbr=on}} through two states over a period over 33 minutes.&lt;ref name="MSSum"&gt;{{cite web| date=2006-7-14| title=Summary of Tornado| publisher=[[National Weather Service]] in Upton, New York| accessdate=2008-11-29|url=http://www.erh.noaa.gov/okx/pns/torjul06.txt}}&lt;/ref&gt;

==Impact==
[[Image:DCP 7760.JPG|thumb|right|Tornado damage near a forested area]]
The tornado took a path through [[Rockland County, New York|Rockland]], [[Westchester County, New York|Westchester]], and [[Fairfield County, Connecticut|Fairfield]] counties, downing or uprooting thousands of trees and damaging several structures, including significant structural damage to the California Closest Warehouse. Six minor injuries were also reported. In all, the tornado inflicted $12.1&amp;nbsp;million (2006&amp;nbsp;[[United States Dollar|USD]]; $12.9&amp;nbsp;million 2008 USD) in damage.&lt;ref name="MSSum"/&gt;

Minor damage was reported in Rockland County. One dock and one boat were damaged by the tornado.&lt;ref name="MSSum"/&gt; After crossing the [[Hudson River]], the tornado entered Westchester County, where the worst of the damage took place. It struck the town of [[Sleepy Hollow, New York|Sleepy Hollow]], damaging roofs and tearing the siding off numerous homes and businesses.&lt;ref name="MSSum"/&gt; A 10&amp;nbsp;foot (3&amp;nbsp;m) tall stained-glass window in the St. Teresa of Avila Church was shattered.&lt;ref name="USAT"/&gt; Afterwards, the town of [[Pocantico Hills, New York|Pocantico Hills]] was struck as the tornado intensified to F2 intensity. Several trees were uprooted and two barns were destroyed. The California Closet Warehouse suffered severe structural damage; two concrete walls were destroyed.&lt;ref name="MSSum"/&gt; An interior staircase, which employees used as a shelter, collapsed causing four injuries. Concrete blocks from the building were blown about, some of which struck cars in a nearby parking lot.&lt;ref name="USAT"/&gt; A nearby [[Comfort Inn]] had part of its roof torn off.&lt;ref name="WESH"&gt;{{cite web| date=2006-7-13|author=Associated Press| title=Tornado Rips Through Suburban New York| publisher=[[Internet Broadcasting|Internet Broadcasting Systems, Inc]]| accessdate=2008-11-30|url=http://www.wesh.com/news/9510358/detail.html}}&lt;/ref&gt; After a [[tornado warning]] was issued, a school near the warehouse was evacuated.&lt;ref name="NYTimes"&gt;{{cite news| author=Lisa W. Foderaro| date=2006-07-13| title=Tornado in Westchester Tosses Around Trees and Damages Property| work=[[The New York Times]]| accessdate=2008-11-30|url=http://www.nytimes.com/2006/07/13/nyregion/13weather.html?pagewanted=print}}&lt;/ref&gt; 

[[File:Westchester Tornado damage1.JPG|thumb|left|An area where numerous trees were knocked down, the white tubes support saplings being grown to re-populate the affected area.]]
As the tornado crossed [[New York State Route 9A]], it picked up a state trooper car and flipped it several times before it fell to the ground; the officer inside suffered only minor injuries.&lt;ref name="USAT"/&gt; Moving towards the east-northeast, the tornado struck the towns of [[Mount Pleasant, New York|Mount Pleasant]] and [[Hawthorne, New York|Hawthorne]], damaging numerous trees and causing minor structural damage.&lt;ref name="MSSum"/&gt; Damage along the [[Saw Mill River Parkway]] prompted officials to shut down a section of the highway near Mount Pleasant.&lt;ref name="CNN"&gt;{{cite news| author= Rose Arce | date=2006-07-13| title=Tornado hits north of Manhattan, Winds damage store, close highway; no serious injuries reported| publisher=[[CNN|Cable News Network]]| accessdate=2008-11-30|url=http://www.cnn.com/2006/WEATHER/07/12/ny.tornado/index.html
}}&lt;/ref&gt;  Trees fell on streets and railroad tracks, halting [[Metro-North Railroad]] service and creating major traffic delays.&lt;ref name="NYTimes"/&gt; After passing by the [[Kensico Reservoir]] in [[Valhalla, New York|Valhalla]], the tornado crossed into [[Connecticut]],&lt;ref name="MSSum"/&gt; where it knocked down numerous power lines, cutting power to about 10,000 residences in the county.&lt;ref name="USAT"/&gt; In all, six people sustained minor injuries and damages amounted to $10.1&amp;nbsp;million (2006 USD).&lt;ref name="Tornado2"/&gt;

The weakening tornado ended its duration in Fairfield County, Connecticut in the town of [[Greenwich, Connecticut|Greenwich]]. Thousands of trees were either uprooted or snapped along the tornado's {{convert|2|mi|km|abbr=on}} path through the state. Minor damage was inflicted upon several structures.&lt;ref name="MSSum"/&gt; The tornado left 1,700 residences in Greenwich without power and blocked six roads. Most of the damage was concentrated to the northwestern corner of the town.&lt;ref name="NYTimes2"&gt;{{cite news| author=Avi Salzman and Anahad O'Connor| date=2006-07-16| title=The Week; Rare Tornado Snaps Trees and Power Lines| publisher=The New York Times| accessdate=2008-12-01|url=http://query.nytimes.com/gst/fullpage.html?res=9F04E2D91F30F935A25754C0A9609C8B63}}&lt;/ref&gt; Damages in the state totaled to  $2&amp;nbsp;million (2006 USD).&lt;ref name="Tornado3"/&gt;

==Aftermath==
In the wake of the tornado, the mayor of Sleepy Hollow declared a town-wide state of emergency.&lt;ref name="ABC7"&gt;{{cite news| author=Eyewitness News| date=2006-07-13| title=Weather Service confirms F2 tornado in area, Sleepy Hollow, Hawthorne hardest hit| publisher=[[ABC News]]| accessdate=2008-11-29|url=http://abclocal.go.com/wabc/story?section=weather&amp;id=4363255}}&lt;/ref&gt; Two hundred emergency personnel responded to the storm.&lt;ref name="LoHUD2"&gt;{{cite news| author=Reka Bala and Glenn Blain| date=2006-07-13| title=Tornado slams Lower Hudson Valley| publisher=[[The Journal News]]| accessdate=2008-12-01|url=http://www.lohud.com/article/20060713/NEWS09/607130345}}&lt;/ref&gt; [[Consolidated Edison]] (conEdison) crews were sent out to repair downed power lines and clear roads. By the next night, power was restored to all but 600 of the previous 10,000 residences without power in [[Westchester County, New York|Westchester]].&lt;ref name="USAT"/&gt; Westchester County opened its Emergency Operations Center after the storm to quickly respond to the event.&lt;ref name="WCBS"&gt;{{cite news| author=Associated Press| date=2006-07-13| title=Westchester County Storm: Let The Clean-Up Begin| publisher=[[WCBS-TV]]| accessdate=2008-11-30|url=http://wcbstv.com/topstories/Tornado.Tornado.Warning.2.236314.html}}&lt;/ref&gt;  Two days after the storm, many of the roads had been cleared and power was fully restored. A recreational path in [[Tarrytown, New York]] was not expected to be open for another two weeks due to numerous fallen trees.&lt;ref name="LoHUD"&gt;{{cite web| date=2006-7-15|author=Candice Ferrette| title=Westchester tornado twists many lives| publisher=The Journal News| accessdate=2008-11-30|url=http://www.lohud.com/apps/pbcs.dll/article?AID=/20060715/NEWS02/607150347}}&lt;/ref&gt; [[Metro-North Railroad]] suspended trains on the Upper Harlem line until 5:00 p.m. EDT (21:00 UTC) for the removal of debris on the tracks. During the time the rails were shut down, southbound passengers were transported by bus.&lt;ref name="NYTimes"/&gt; All trains were back on schedule by 7:00 p.m. EDT (23:00 UTC).&lt;ref name="LoHUD2"/&gt;

==See also==
*[[List of North American tornadoes and tornado outbreaks]]
*[[Tornadoes_of_2006#July_11-12|Tornadoes of 2006]]
*[[List of Connecticut tornadoes]]

== References ==
{{Reflist|2}}

==External links==
*[http://wcbstv.com/video/?id=89570@wcbs.dayport.com Doppler Radar image of the tornadic supercell nearing Tarrytown]
*[http://www.youtube.com/watch?v=_fLZLrZAB0M Video of the tornado damage in Westchester]
*[http://wcbstv.com/topstories/Tornado.Tornado.Warning.2.236314.html WCBS article and video of damage/press reports of the tornado]

{{featured article}}
[[Category:F2 tornadoes]]
[[Category:New York tornadoes]]
[[Category:Connecticut tornadoes]]
[[Category:Tornadoes of 2006]]
[[Category:2006 in the United States]]


"""

qe = QueryExecutor()
qe.setOutputFileDirectoryName('lol')
#qe.sethtml()
qe.setNumberOfProcesses(5)
qe.setNumberOfBytes(2000000000)
qe.setTextValue(input_text)
#print(qe.getTextValue())
#qe.setCompress(True)
#qe.setPreserveLinks(True)
qe.runQuery()
print(qe.result())

