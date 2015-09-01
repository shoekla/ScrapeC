from flask import Flask
from flask import request
from flask import render_template
import scrape
import time
import os
app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post(name=None,what=None,timeA=None,face=None,gog=None,twit=None,socA=None,res=None,length=None,typeA=None):
	name = request.form['name']
	what = request.form['what']
	startTime=time.time()
	typeA="Something"
	socA=False
	res=[]
	if name.startswith("www"):
		name=str("http://"+name)
	abir=scrape.isLink(str(name))
	if abir==True:
		try:
			typeA="Link"
			if what=="links":
				res=scrape.crawlLink(name)
				what="Link Aggregated"
			elif what=="social":
				res=scrape.crawlLinkScoial(name)
				gog=scrape.getGoogLink(name)
				twit=scrape.getTwitLink(name)
				face=scrape.getFaceLink(name)
				socA=True
				what="Social Media"
			elif what=="nothing":
				return render_template('bad.html')
			elif what=="info":
				res=scrape.getDataTwo(name)
				what= "Information Aggregated"
			elif what=="image":
				res=scrape.linkImg(name)
				what="Images"
			elif what=="contact":
				res=scrape.contactLink(name)
				what="Contact Information From Link"
			elif what=="video":
				res=scrape.linkVid(name)
				what="Videos Aggregated"
			elif what=="pdf":
				res=scrape.crawlPDF(name)
				what="PDFs Aggregated"

		except:
			typeA="Search Query"
			if what=="links":
				res=scrape.SearchCrawl(name)
				what="Link Aggregated"
			elif what=="info":
				res=scrape.SearchInfo(name)
				what= "Information Aggregated"
			elif what=="contact":
				res=scrape.contactsA(name)
				what="Contact Information"
			elif what=="nothing":
				return render_template('bad.html',name=name)
			elif what=="image":
				res=scrape.searchImg(name)
				what="Images"
			elif what=="social":
				res=scrape.SearchSocial(name)
				face=scrape.getFacebook(name)
				twit=scrape.getTwitter(name)
				gog=scrape.getGooglePlus(name)
				socA=True
				what="Social Media"
			elif what=="video":
				res=scrape.getVideoSearch(name)
				what="Videos Aggregated"
			elif what=="pdf":
				res=scrape.SearchCrawlPDF(name)
				what="PDFs Aggregated"


	else:
		typeA="Search Query"
		if what=="links":
			res=scrape.SearchCrawl(name)
			what="Link Aggregated"
		elif what=="info":
			res=scrape.SearchInfo(name)
			what= "Information Aggregated"
		elif what=="contact":
			res=scrape.contactsA(name)
			#[[[u'http://www.utexas.edu/faculty/'], []], [[u'http://www.utexas.edu/academics/areas-of-study'], []], [[u'http://www.utexas.edu/faculty/council/'], ['fc@austin.utexas.edu']], [[u'https://facultyjobs.utexas.edu/'], ['evpp.aps@utlists.utexas.edu']], [[u'http://www.utexas.edu/police/'], ['trecs.web@austin.utexas.edu', 'Phone: 512-471-4441']], [[u'http://www.cm.utexas.edu/faculty-and-research/faculty-directory'], ['anslyn@austin.utexas.edu', 'cbaiz@cm.utexas.edu', 'ajbard@mail.utexas.edu', 'jbrodbelt@cm.utexas.edu', 'campion@mail.utexas.edu', 'jrc@utexas.edu', 'acowley@cm.utexas.edu', 'crooks@cm.utexas.edu', 'gbdong@cm.utexas.edu', 'liviase@utexas.edu', 'ron@ices.utexas.edu', 'henkelman@utexas.edu', 'bholliday@cm.utexas.edu', 'smh@cm.utexas.edu', 'iversonb@austin.utexas.edu', 'rajones@cm.utexas.edu', 'adriankc@utexas.edu', 'mkrische@cm.utexas.edu', 'dalaude@austin.utexas.edu', 'h.w.liu@mail.utexas.edu', 'makarov@cm.utexas.edu', 'sfmartin@mail.utexas.edu', 'mullins@che.utexas.edu', 'emilyque@cm.utexas.edu', 'roberts@cm.utexas.edu', 'mrose@cm.utexas.edu', 'sessler@cm.utexas.edu', 'jshear@cm.utexas.edu', 'jfstanton@gmail.com', 'stevenson@cm.utexas.edu', 'davandenbout@mail.utexas.edu', 'lwebb@cm.utexas.edu', 'willson@che.utexas.edu', 'Phone: 512-471-0068', 'Phone: 512-471-3761', 'Phone: 512-471-0028', 'Phone: 512-471-3012', 'Phone: 512-232-9083', 'Phone: 512-471-7484', 'Phone: 512-475-8674', 'Phone: 512-232-8220', 'Phone: 512-232-5415', 'Phone: 512-471-4179', 'Phone: 512-471-8491', 'Phone: 512-471-0312', 'Phone: 512-471-5053', 'Phone: 512-471-1706', 'Phone: 512-471-2977', 'Phone: 512-232-5892', 'Phone: 512-232-3317', 'Phone: 512-232-7811', 'Phone: 512-471-4575', 'Phone: 512-471-3915', 'Phone: 512-471-5817', 'Phone: 512-471-4490', 'Phone: 512-475-9450', 'Phone: 512-471-4456', 'Phone: 512-471-5009', 'Phone: 512-232-1454', 'Phone: 512-232-9160', 'Phone: 512-232-2824', 'Phone: 512-471-9361', 'Phone: 512-471-4342']], [[u'https://courses.utexas.edu/'], []], [[u'http://www.utah.edu/faculty/'], ['Phone: 801-581-7200']], [[u'http://www.utexas.edu/staff/'], []], [[u'http://history.utah.edu/faculty/faculty-directory-full.php'], ['u0984276@utah.edu', 'u0693493@utah.edu', 'presidentialsearch@utahsbr.edu']], [[u'http://history.utah.edu/faculty/'], ['presidentialsearch@utahsbr.edu']], [[u'https://faculty.utah.edu/'], ['Academic-IT-Help@utah.edu', 'academic-it-help@utah.edu', 'Phone: 801.585.5355']], [[u'http://www.ut.edu/directory.aspx'], []], [[u'http://www.utah.edu/staff/'], ['Phone: 801-581-7200']], [[u'http://www.utk.edu/facultyandstaff/'], ['webteam@utk.edu', 'Phone: 865-974-1000']], [[u'http://www.dallasnews.com/news/education/headlines/20150731-ut-dallas-can-t-diversify-faculty-fast-enough-to-keep-up-with-student-body.ece'], []], [[u'http://en.wikipedia.org/wiki/List_of_University_of_Texas_at_Austin_faculty'], []], [[u'http://en.wikipedia.org/wiki/List_of_University_of_Texas_at_Austin_faculty#Administration'], []], [[u'http://en.wikipedia.org/wiki/List_of_University_of_Texas_at_Austin_faculty#School_of_Architecture'], []], [[u'http://en.wikipedia.org/wiki/List_of_University_of_Texas_at_Austin_faculty#College_of_Communication'], []], [[u'http://www.uttyler.edu/facultystaff/'], ['enroll@uttyler.edu', 'web@uttyler.edu', 'Phone: 903.566.7203', 'Phone: 903.566.7068', 'Phone: 903.566.7000', 'Phone: 903.566.7783']], [[u'http://faculty.utsa.edu/'], ['facultycenter@utsa.edu', 'Phone: 210-458-4011', 'Phone: 210-458-4242']], [[u'http://www.utk.edu/'], ['webteam@utk.edu', 'Phone: 865-974-1000']], [[u'http://www.utah.gov/'], []], [[u'http://www.uvu.edu/facstaff/'], ['instantinfo@uvu.edu', 'servicedesk@uvu.edu', 'Phone: 801.863.8888']], [[u'https://law.utexas.edu/faculty/'], []], [[u'http://www.utsystem.edu/'], ['Phone: 1:10,2:9,3:8']], [[u'http://www.utdallas.edu/faculty/'], []], [[u'http://www.uta.edu/uta/'], ['Phone: 817-272-2011']], [[u'http://www.employment.utah.edu/faculty/index.php'], ['heather.call@utah.edu', 'employment@utah.edu', 'webmaster@hr.utah.edu', 'Phone: 801.581.2169']], [[u'http://www.texassports.com/'], []], [[u'http://www.utsystem.edu/directory'], ['Phone: 1:10,2:9,3:8']], [[u'https://law.utexas.edu/faculty-resources/'], []], [[u'http://www.uttyler.edu/facultystaff/faculty-search.php'], ['enroll@uttyler.edu', 'web@uttyler.edu', 'Phone: 903.566.7000', 'Phone: 903.566.7783']], [[u'http://texassports.com/?path=football'], []], [[u'http://medicine.utah.edu/faculty/'], []], [[u'http://www.civil.utah.edu/faculty'], ['barber@civil.utah.edu', 'bartlett@civil.utah.edu', 'bordelon@civil.utah.edu', 'burian@eng.utah.edu', 'jchambers@civil.utah.edu', 'dan.fagnant@utah.edu', 'ram.goel@utah.edu', 'hong@civil.utah.edu', 'luis.ibarra@utah.edu', 'tatjana.jevremovic@utah.edu', 'lawton@civil.utah.edu', 'Azaree.Lintereur@utah.edu', 'cathy.liu@utah.edu', 'luther.mcdonald@utah.edu', 'b.j.mcpherson@utah.edu', 'chris@civil.utah.edu', 'christine.pomeroy@utah.edu', 'richard.jon.porter@utah.edu', 'romero@civil.utah.edu', 'doug.schmucker@utah.edu', 'rebecca.brannon@utah.edu', 'bmurphy@egi.utah.edu', 'gjohnson@egi.utah.edu', 'gjohnson@egi.utah.edujjohnson', 'egi.utah.edujjohnson@reaveley.com', 'william.johnson@utah.edu', 'rlevey@egi.utah.edu', 'dp@mmc-pm.com', 'gms@asp-llc.com', 'nucpower@sbcglobal.net', 'milan@trafficlab.utah.edu', 'deckhoff@xmission.com', 'reaveley@civil.utah.edu', 'webmaster@civil.utah.edu', 'Phone: 102,1,386,55', 'Phone: 801.585.7710', 'Phone: 801.587.7726', 'Phone: 801.581.3578', 'Phone: 801.585.5721', 'Phone: 801.581.3155', 'Phone: 801.585.2877', 'Phone: 801.581.6110', 'Phone: 801.581.7232', 'Phone: 801.585.9307', 'Phone: 801.587.9696', 'Phone: 801.585.3947', 'Phone: 801.581.6785', 'Phone: 801.587.8858', 'Phone: 801.581.7768', 'Phone: 801.585.7961', 'Phone: 801.585.3991', 'Phone: 801.585.7300', 'Phone: 801.585.1290', 'Phone: 801.587.7725', 'Phone: 801.587.3815', 'Phone: 801.581.6931', 'Phone: 801.581.6623', 'Phone: 801.585.5982', 'Phone: 801.581.6151', 'Phone: 801.486.3883', 'Phone: 801.581.5033', 'Phone: 801.585.3826']], [[u'http://www.civil.utah.edu/people'], ['webmaster@civil.utah.edu', 'Phone: 102,1,386,55']], [[u'http://www.utsports.com/directory/'], []], [[u'http://www.utdallas.edu/'], []], [[u'http://facultyclub.utah.edu/'], []], [[u'http://www.utah.gov/government/'], []], [[u'http://www.usu.edu/'], []], [[u'http://www.utsouthwestern.edu/'], ['myname@email.com', 'myfriend@email.com', 'Phone: 214-645-8300', 'Phone: 214-648-3111']], [[u'http://www.usu.edu/facultystaff/'], []], [[u'http://www.math.utah.edu/people/faculty.html'], ['tombrennan@waterfordschool.org', 'sarahjean.hoggan@utah.edu', 'images/small/sarahjean.hoggan@utah.edu.jpg', 'rod.millar@utah.edu', 'cstone@dsdmail.net', 'webmaster@math.utah.edu', 'Phone: 801-359-4452']], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#History'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#Campus'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#Organization_and_administration'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#Academics'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#Research'], []], [[u'http://en.wikipedia.org/wiki/University_of_Texas_at_Austin#Student_life'], []], [[u'http://www.utpa.edu/faculty-staff/'], []], [[u'http://www.nuclear.utah.edu/faculty'], ['tatjana.jevremovic@utah.edu', 'luther.mcdonald@utah.edu', 'mb@sci.utah.edu', 'bordelon@civil.utah.edu', 'otakuye.conroy@utah.edu', 'ganesh@cs.utah.edu', 'paolo.gondolo@utah.edu', 'grissomc@chem.utah.edu', 's.guruswamy@utah.edu', 'michael.hoepfner@utah.edu', 'crj@sci.utah.edu', 'jj.magda@utah.edu', 'jmclennan@egi.utah.edu', 'ilija.miskovic@utah.edu', 'sanja.miskovic@utah.edu', 'scott.miller@hsc.utah.edu', 'Mano.Misra@utah.edu', 't.ring@m.cc.utah.edu', 'romero@civil.utah.edu', 'shad.roundy@utah.edu', 'allen@sci.utah.edu', 'gms@asp-llc.com', 'michael.simpson@utah.edu', 'jamesina.simpson@utah.edu', 'mikhail.skliar@utah.edu', 'smith@crism.utah.edu', 'jjthomp@sandia.gov', 'zhou@eng.utah.edu', 'webmaster@civil.utah.edu']], [[u'http://www.nuclear.utah.edu/people'], ['webmaster@civil.utah.edu']], [[u'http://dentistry.utah.edu/facultyprofile.php?facultyID=u6003088'], []], [[u'http://www.ma.utexas.edu/'], ['Phone: 46,16,320,40', 'Phone: 46,40,245,65']], [[u'http://www.utoledo.edu/menu/faculty_staff.html'], []], [[u'http://www.uta.edu/coed/faculty-staff/index.php'], ['Phone: 817-272-2591', 'Fax: 817-272-2530']], [[u'https://med.uth.edu/'], ['Ebony.Wolford@uth.tmc.edu', 'ms.communications@uth.tmc.edu', 'Phone: 713-500-7452', 'Phone: 713.500.4472']], [[u'http://www.mccombs.utexas.edu/'], []], [[u'http://www.utoledo.edu/facsenate/'], ['facultysenate@utoledo.edu', 'webmaster@utoledo.edu', 'Phone: 419.530.2112', 'Phone: 419.530.2114']], [[u'https://faculty.utah.edu/u0130713%20/teaching/index.hml'], ['Academic-IT-Help@utah.edu', 'Phone: 801.585.5355']], [[u'http://utahsenatestaff.com/'], []], [[u'http://profiles.utsouthwestern.edu/'], ['webservices@utsouthwestern.edu', 'Phone: 214-645-8300', 'Phone: 214-456-7000', 'Phone: 214-648-3111']], [[u'http://sites.utexas.edu/rfsa/'], []], [[u'https://dentistry.uth.edu/departments'], []], [[u'http://www.math.utah.edu/'], ['webmaster@math.utah.edu']], [[u'http://www.utsouthwestern.edu/fis/index.html'], ['myname@email.com', 'myfriend@email.com', 'webservices@utsouthwestern.edu', 'VLYi2FzCtIp_w+MahlDZrKsPf3ET8W@X1jO-GHAJnbNcv.QoRy6U05u9xqkdS7m4gBe\\', 'Phone: 214-645-8300', 'Phone: 214-648-3111']], [[u'http://www.lib.utexas.edu/d7/geology/research-guide/big-bend/general-sources'], []], [[u'http://www.lib.utexas.edu/subject'], ['b.deputy@austin.utexas.edu', 'ldallas@austin.utexas.edu', 'rrosenberg@austin.utexas.edu', 'ardis@austin.utexas.edu', 'prascoe@austin.utexas.edu', 'n.elder@austin.utexas.edu', 'roxanne.bogucka@austin.utexas.edu', 'pgmoreno@austin.utexas.edu', 'carolynlouise@austin.utexas.edu', 'd.correa@austin.utexas.edu', 'winchester@austin.utexas.edu', 'katiepiercemeyer@austin.utexas.edu', 'lschwartz@austin.utexas.edu', 'm.rader@austin.utexas.edu', 'msu@austin.utexas.edu', 'mwhite@austin.utexas.edu', 'lay@austin.utexas.edu', 'aj@austin.utexas.edu', 'flaxbart@austin.utexas.edu', 'wjkopplin@austin.utexas.edu', 'beth@austin.utexas.edu', 'jhedstrom@austin.utexas.edu', 'kolodney@austin.utexas.edu', 'merry@austin.utexas.edu', 'drtgeol@austin.utexas.edu', 'h.chapa@austin.utexas.edu', 'skilgore@austin.utexas.edu', 'j.montelongo@austin.utexas.edu', 'mgutierrez@austin.utexas.edu', 'jwdobbs@austin.utexas.edu', 'l.dehart@austin.utexas.edu', 'david.hunter@austin.utexas.edu', 'cynthfisher@austin.utexas.edu', 'elisenacca@austin.utexas.edu', 'krystal@austin.utexas.edu', 'micheleo@austin.utexas.edu', 's.brandt@austin.utexas.edu']], [[u'http://www.lib.utexas.edu/geology/research-guide'], ['drtgeol@austin.utexas.edu', 'georequests@lib.utexas.edu']], [[u'http://www.chem.utah.edu/'], ['Phone: 801-581-8433']], [[u'http://profiles.uthscsa.edu/'], ['dcats@uthscsa.edu', 'webadmin@uthscsa.edu']], [[u'http://pages.utdallas.edu/'], []], [[u'http://www.utc.edu/about/faculty-staff-resources.php'], []], [[u'http://econ.bus.utk.edu/department/faculty.asp'], ['wneilson@utk.edu', 'kbaker5@utk.edu', 'lbray3@utk.edu', 'dbruce@utk.edu', 'Dbueckma@utk.edu', 'dbueckma@utk.edu', 'mburton3@utk.edu', 'carruthers@utk.edu', 'dclark3@utk.edu', 'bcompton@utk.edu', 'billfox@utk.edu', 'jgauger@utk.edu', 'sgilpatr@utk.edu', 'mharris@utk.edu', 'jhollad3@utk.edu', 'ckauffma@utk.edu', 'lkessler@utk.edu', 'jlarivi1@utk.edu', 'llima@utk.edu', 'mmohsin@utk.edu', 'mmurray1@utk.edu', 'rsantore@utk.edu', 'gschaur@utk.edu', 'cbsims@utk.edu', 'ksims12@utk.edu', 'cvossler@utk.edu', 'wanamaker@utk.edu', 'economics@utk.edu', 'haslam@utk.edu', 'Phone: 27,19,492,63', 'Phone: 30,62,528,97', 'Phone: 865-974-5591', 'Phone: 865-974-3303', 'Fax: 865-974-4601', 'Phone: 865-974-5061', 'Fax: 865-974-1766', 'Phone: 865-974-1000']], [[u'http://csd.utexas.edu/center/'], ['UTSpeechandHearing@austin.utexas.edu', 'comm-webmaster@austin.utexas.edu', 'Phone: 512.471.3841', 'Fax: 512.232.1804', 'Phone: 512/471-3841', 'Phone: 512/232-5004', 'Phone: 512-471-4119', 'Fax: 512-471-2957', 'Phone: 512-471-3841', 'Fax: 512-232-1804']], [[u'http://bas.utk.edu/academic-programs/masters/business-analytics/default.asp'], ['bas@utk.edu', 'haslam@utk.edu', 'Phone: 27,20,814,64', 'Phone: 30,62,528,97', 'Phone: 865-974-5544', 'Fax: 865-974-2490', 'Phone: 865-974-5061', 'Fax: 865-974-1766', 'Phone: 865-974-1000']], [[u'http://www.canyonsdistrict.org/index.php?option=com_k2&view=item&id=703&Itemid=613'], ['communications@canyonsdistrict.org']], [[u'http://0.r.msn.com/?ld=d3zV9rkEXythPPUqi-eKDy_TVUCUxp6OR4VXO7ScEn8SDyPSNbOF1o9f8vln-AaBAwmb0B2zrcIHbkYeTan27LznMdEgR9gbHRL9wueG6dWrIzp5fFAaJ-SWIz-5BPmSAfFK_JJwUpmFeHYQ1PwbvVQYQt0tZSefxPhQWhyRsFzph0z9WD&u=www.universityofphoenixinfo.com%2fc%2fuop-education%2findex.php%3fs%3dmsn%26c%3duope%26tp3%3db%26k%3dUtah%2520community%2520colleges'], []], [[u'http://academic-affairs.utah.edu/office-for-faculty/administrative-staff-resources/'], ['Phone: 801.581.7200']], [[u'http://www.nature.com/naturejobs/science/jobs/540399-sustaining-biodiversity-tenured-faculty-position'], []], [[u'http://www.nature.com/naturejobs/science/'], []], [[u'http://www.nature.com/naturejobs/science/jobs'], []], [[u'http://www.utahjobnetwork.com/j/t-staff-research-assistant-e-university-of-utah-l-salt-lake-city,-ut-jobs-j13480440.html'], ['info@utahjobnetwork.com', 'Phone: 801-581-2300']], [[u'http://faculty.utsa.edu/events/department-of-defense-panel-discussion/'], ['jaclyn.shaw@utsa.edu', 'facultycenter@utsa.edu', 'Phone: 210-458-4011', 'Phone: 210-458-4242']], [[u'https://cehs.usu.edu/research/about-us/staff'], []], [[u'http://www.thecoolersguys.com/ut/coolers-in-oasis/'], []], [[u'http://www.thecoolersguys.com/ut/'], []], [[u'http://mscm.bus.utk.edu/Department/faculty/Rodrigues.asp'], ['arodri23@utk.edu', 'lmurray6@utk.edu', 'haslam@utk.edu', 'Phone: 27,19,753,61', 'Phone: 30,66,519,97', 'Phone: 865.974.1872', 'Phone: 865-974-5311', 'Fax: 865-974-1932', 'Phone: 865-974-5061', 'Fax: 865-974-1766', 'Phone: 865-974-1000']], [[u'http://jobs.utah.gov/jsp/wi/utalmis/oijoborder.do?ordernum=9843466'], []], [[u'https://faculty.utah.edu/u0946359%20/teaching/index.hml'], ['Academic-IT-Help@utah.edu', 'Phone: 801.585.5355']], [[u'https://www.higheredjobs.com/search/details.cfm?JobCode=176110421&Title=Medical%20Assistant%20%2A%2Ain%20St%2E%20George%2C%20UT%2A%2A'], []], [[u'https://www.higheredjobs.com/search/'], []], [[u'https://www.higheredjobs.com/search/advanced.cfm'], []], [[u'http://www.utexas.edu/nursing/faculty/'], ['webmaster@mail.nur.utexas.edu']], [[u'http://www.utexas.edu/cola/depts/history/faculty/list.php'], []]]	
			what="Contact Information"
		elif what=="nothing":
			return render_template('bad.html',name=name)
		elif what=="image":
			res=scrape.searchImg(name)
			what="Images"
		elif what=="social":
			res=scrape.SearchSocial(name)
			face=scrape.getFacebook(name)
			twit=scrape.getTwitter(name)
			gog=scrape.getGooglePlus(name)
			socA=True
			what="Social Media"
		elif what=="video":
			res=scrape.getVideoSearch(name)
			what="Videos Aggregated"
		elif what=="pdf":
			res=scrape.SearchCrawlPDF(name)
			what="PDFs Aggregated"
	length=len(res)

	timeA = time.time() - startTime
	return render_template('results.html',typeA=typeA,name=name,what=what,timeA=timeA,twit=twit,gog=gog,face=face,socA=socA,res=res,length=length)
@app.route('/home')
def home():
	return render_template("index.html")
@app.route('/link')
def link(res=None):
	res=[["https://www.facebook.com/","test1 dsfsdfsd"],["http://flask.pocoo.org/docs/0.10/tutorial/templates/","test 2 sadfasdfa"],["https://www.google.com/","Google!!!!!!!!!!!!"]]
	return render_template('test.html',res=res)


if __name__ == '__main__':
    app.run()


