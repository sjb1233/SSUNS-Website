from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

COMMITTEE = (
	('African Union', 'African Union'),
	('United Nations General Assembly','United Nations General Assembly'),
	('United Nations Framework on Climate Change: COP 22','United Nations Framework on Climate Change: COP 22'),
	('The Commission on the Status of Women','The Commission on the Status of Women'),
	('United Nations Economic and Social Commission for Asia and the Pacific','United Nations Economic and Social Commission for Asia and the Pacific'),
	('United Nations Educational, Scientific and Cultural Organization','United Nations Educational, Scientific and Cultural Organization'),
	('World Health Organization','World Health Organization'),
	('8th Congress','8th Congress'),
	('Canadian Confederation','Canadian Confederation'),
	('International Atomic Energy Agency 2017','International Atomic Energy Agency 2017'),
	('Czechoslovakia Government 1990','Czechoslovakia Government 1990'),
	('United Nations Office for Outer Space Affairs and International Civil Aviation Organization','United Nations Office for Outer Space Affairs and International Civil Aviation Organization'),
	('Venezuelan National Assembly','Venezuelan National Assembly'),
	('National Football League 2016','National Football League 2016'),
	('Microsoft','Microsoft'),
	('Apollo 13','Apollo 13'),
	('World War II','World War II'),
	('Ad Hoc','Ad Hoc'),
	("The Handmaid's Tale","The Handmaid's Tale"),
	("Queen Anne's Revenge","Queen Anne's Revenge"),
	('Salem Village',"Salem Village"),
	('Third Servile Revolt','Third Servile Revolt'),
	('First Scottish War of Independence','First Scottish War of Independence')
	)

# Create your models here.
class RegistrationForm(models.Model):
	# Name of school - string
	# Will this be the first time? T/F 
	# Faculty Advisor: 
	# Phone number
	# First + Last
	# Email
	# Personal alt email

	# Head Delegate:
	# First + Last
	# email
	# Mailing Address: Address Line 1, Line 2, City, State/Province/Region, Postal Code/Zip, Country
	# School's Number + Fax

	# Committee Preference (choose 5):

	# Previous Experience

	# Delegate + Payment Info
	# Yes or no to paypal
	# Number of delegates + 85*number*1.03 if paypal

	# Media Consent 
	Faculty_Advisor_Email = models.EmailField(help_text="<i><small><small>Please enter a unique email address. The registration response will be sent to this email.</small></small></i>")
	Faculty_Advisor_Name = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter your first and last name</small></small></em>")
	Name_of_School = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter the name of your institution</small></small></em>")
	
	BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
	PAYMENT_CHOICES = ((True, 'Online - Paypal'), (False, 'Cheque by Mail'))
	Will_this_be_your_first_time_attending_SSUNS = models.BooleanField(choices=BOOL_CHOICES, default=True, help_text="<p><br><h4>Contact Details</h4></p>")
	Payment_Method = models.BooleanField(choices=PAYMENT_CHOICES, default=False, help_text="<em><small><small>Please specify your payment method. <b> Note: Paypal payments include a 3.00% paypal fee, applied to the total amount owed.</b> </em></small></small><br><br>")
	Media_Consent = models.BooleanField(choices=BOOL_CHOICES, default=True, help_text="<small><small><em>Every year, we hire photographers to capture every moment of SSUNS when it comes to the experience of the staffers, delegates and faculty advisors alike. In an effort to promote our conference, we would like to use these pictures on our website/brochure/pamphlets for others to see and learn more about SSUNS. Would your school be amenable for SSUNS to use such photos?</em></small></small>")
	Are_there_any_allergies_or_concerns_that_we_should_know_about = models.BooleanField(choices=BOOL_CHOICES, default=False)
	Please_Specify = models.TextField(blank=True, null=True)

	Faculty_Advisor_Alternate_Email = models.EmailField(default='', help_text="<em><small><small>Please enter a unique personal email address.</small></small></em>")

	Head_Delegate_Name = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter the head delegate's first and last name</small></small></em>")
	Head_Delegate_Email = models.EmailField(default='', help_text="<em><small><small>Please enter a unique email address.</small></small></em><p><br><h4>Mailing Address</h4></p><p><em>Please enter the mailing address of your instituiton</em></p>")

	#Mailing
	Address_Line_1 = models.CharField(max_length=300, blank=False, null=True)
	Address_Line_2 = models.CharField(max_length=300, blank=True, null=True)
	City = models.CharField(max_length=50, blank=False, null=True)
	Province_or_State_or_Region = models.CharField(max_length=50, blank=False, null=True)
	Country = CountryField(blank=False, blank_label='Select Country')
	Phone = models.CharField(max_length=30, blank=False, null=True)
	Cell_Phone = models.CharField(max_length=30, blank=False, null=True, help_text="<br><br>")
	Cell_Phone_of_Head_Delegate = models.CharField(max_length=30, blank=True, null=True, help_text="<em><small><small>This field is not required, but it is helpful to be able to contact a delegate if the faculty advisor is unavailable.</em></small></small>")
	Fax = models.CharField(max_length=30, blank=True, null=True, help_text="<p><br><h4>Committee Preferences (Max 3 per Category)</h4></p>")

	#Committee Preferences
	CHOICES_GA = (('United Nations General Assembly', 'United Nations General Assembly'), ('United Nations Framework Convention on Climate Change', 'United Nations Framework Convention on Climate Change'),('United Nations Educational, Scientific and Cultural Organization', 'United Nations Educational, Scientific and Cultural Organization'),('African Union', 'African Union'),('Commission on the Status of Women', 'Commission on the Status of Women'), ('United Nations Economic and Social Council for Asia and the Pacific','United Nations Economic and Social Council for Asia and the Pacific'),('World Health Organization','World Health Organization'))
	CHOICES_SA = (('Bilingual: Canadian Confederation', 'Bilingual: Canadian Confederation'), ('National Football League 2016', 'National Football League 2016'),('Microsoft Board of Directors', 'Microsoft Board of Directors'),('International Atomic Energy Agency 2017', 'International Atomic Energy Agency 2017'),('Venezuelan National Assembly', 'Venezuelan National Assembly'), ('8th United States Congress 1803','8th United States Congress 1803'),('Czechoslovak Government 1990','Czechoslovak Government 1990'),('United Nations Office for Outer Space Affairs and International Civil Aviation Organization - 3rd International Symposium 2017','United Nations Office for Outer Space Affairs and International Civil Aviation Organization - 3rd International Symposium 2017'))
	CHOICES_CRI = (('Ad Hoc', 'Ad Hoc'), ('Literary: The Handmaids Tale', 'Literary: The Handmaids Tale'),('NASA: Apollo 13', 'NASA: Apollo 13'),('Crew of the Queen Annes Revenge', 'Crew of the Queen Annes Revenge'),('Salem Village 1692', 'Salem Village 1692'), ('Britain WWII','Britain WWII'),('Joint Crisis: 3rd Servile Revolt','Joint Crisis: 3rd Servile Revolt'),('Joint Crisis: Scottish War of Independence','Joint Crisis: Scottish War of Independence'))
	General_Assemblies_and_ECOSOC = MultiSelectField(default='United Nations General Assembly', choices=CHOICES_GA, max_choices=3)
	Specialized_Agencies = MultiSelectField(default='Bilingual: Charlottetown Conference', choices=CHOICES_SA, max_choices=3)
	Crises = MultiSelectField(default='Ad Hoc', choices=CHOICES_CRI, max_choices=3)
	

	DEL_CHOICES = ((1, 'Number of Delegates: 1 --- Total: $190.00'), (2, 'Number of Delegates: 2 --- Total: $285.00'),(3, 'Number of Delegates: 3 --- Total: $380.00'),(4, 'Number of Delegates: 4 --- Total: $475.00'),(5, 'Number of Delegates: 5 --- Total: $570.00'),(6, 'Number of Delegates: 6 --- Total: $665.00'),(7, 'Number of Delegates: 7 --- Total: $760.00'),(8, 'Number of Delegates: 8 --- Total: $855.00'),(9, 'Number of Delegates: 9 --- Total: $950.00'),(10, 'Number of Delegates: 10 --- Total: $1045.00'),(11, 'Number of Delegates: 11 --- Total: $1140.00'),(12, 'Number of Delegates: 12 --- Total: $1235.00'),(13, 'Number of Delegates: 13 --- Total: $1330.00'),(14, 'Number of Delegates: 14 --- Total: $1425.00'),(15, 'Number of Delegates: 15 --- Total: $1520.00'),(16, 'Number of Delegates: 16 --- Total: $1615.00'),(17, 'Number of Delegates: 17 --- Total: $1710.00'),(18, 'Number of Delegates: 18 --- Total: $1805.00'),(19, 'Number of Delegates: 19 --- Total: $1900.00'),(20, 'Number of Delegates: 20 --- Total: $1995.00'),(21, 'Number of Delegates: 21 --- Total: $2090.00'),(22, 'Number of Delegates: 22 --- Total: $2185.00'),(23, 'Number of Delegates: 23 --- Total: $2280.00'),(24, 'Number of Delegates: 24 --- Total: $2375.00'),(25, 'Number of Delegates: 25 --- Total: $2470.00'),(26, 'Number of Delegates: 26 --- Total: $2565.00'),(27, 'Number of Delegates: 27 --- Total: $2660.00'),(28, 'Number of Delegates: 28 --- Total: $2755.00'),(29, 'Number of Delegates: 29 --- Total: $2850.00'),(30, 'Number of Delegates: 30 --- Total: $2945.00'),(31, 'Number of Delegates: 31 --- Total: $3040.00'),(32, 'Number of Delegates: 32 --- Total: $3135.00'),(33, 'Number of Delegates: 33 --- Total: $3230.00'),(34, 'Number of Delegates: 34 --- Total: $3325.00'),(35, 'Number of Delegates: 35 --- Total: $3420.00'),(36, 'Number of Delegates: 36 --- Total: $3515.00'),(37, 'Number of Delegates: 37 --- Total: $3610.00'),(38, 'Number of Delegates: 38 --- Total: $3705.00'),(39, 'Number of Delegates: 39 --- Total: $3800.00'),(40, 'Number of Delegates: 40 --- Total: $3895.00'),(41, 'Number of Delegates: 41 --- Total: $3990.00'),(42, 'Number of Delegates: 42 --- Total: $4085.00'),(43, 'Number of Delegates: 43 --- Total: $4180.00'),(44, 'Number of Delegates: 44 --- Total: $4275.00'),(45, 'Number of Delegates: 45 --- Total: $4370.00'),(46, 'Number of Delegates: 46 --- Total: $4465.00'),(47, 'Number of Delegates: 47 --- Total: $4560.00'),(48, 'Number of Delegates: 48 --- Total: $4655.00'),(49, 'Number of Delegates: 49 --- Total: $4750.00'),(50, 'Number of Delegates: 50 --- Total: $4845.00'),(51, 'Number of Delegates: 51 --- Total: $4940.00'),(60, 'Number of Delegates: 60 --- Total: $5795.00'))
	# ,validators=[MinValueValidator(1),MaxValueValidator(50)]
	Number_of_Delegates = models.IntegerField(default=1, blank=False,choices=DEL_CHOICES, help_text="<em><small><small>There must be between 1 and 50 (inclusive) delegates. If you desire more delegates, email the Chargee d'Affaires.<b>Total is the sum of the delegation fee and per-delegate fee. NOTE: Schools located in Canada pay in CAD, and schools located in the United States and abroad pay in USD</b></em></small></small>")

	Previous_Model_UN_Experience = models.TextField(blank=False, null=True, help_text="<i><small><small>Please describe your delegation's previous Model United Nations experiences, including past attendance/performance at SSUNS (if applicable), attendance/performance at other Model United Nations conferences, and any conferences organized by your delegation or school. If you wish, you may include this information in a separate e-mail addressed to Wendy Zhang, Charge d'Affaires (schools@ssuns.org).</small></small></i>")

	Secretariat_Log = models.TextField(blank=True, null=True, default='ex. BY SSUNS IT: This school changed from 9 dels to 10 dels', help_text="SSQUAD: Fill this out if you make any changes, yo!")
	Invoice_Sent = models.BooleanField(choices=BOOL_CHOICES, default=False)
	Paid = models.BooleanField(choices=BOOL_CHOICES, default=False)

	date = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.Faculty_Advisor_Email

class DelegateInput(models.Model):
	Name_of_School = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter the name of your institution. Make sure the name is spelt the exact same as specified on the dashboard. Do not put accents in the name, or the submission will not work.</small></small></em>")
	Delegate_1 = models.CharField(max_length=120, blank=False, null=True)
	Delegate_1_Country = models.CharField(max_length=120, blank=False, null=True)
	Delegate_1_Committee = models.CharField(max_length=120, blank=False, null=True, choices=COMMITTEE)

	Delegate_2 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_2_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_2_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_3 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_3_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_3_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_4 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_4_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_4_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_5 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_5_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_5_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_6 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_6_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_6_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_7 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_7_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_7_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_8 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_8_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_8_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_9 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_9_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_9_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Delegate_10 = models.CharField(max_length=120, blank=True, null=True)
	Delegate_10_Country = models.CharField(max_length=120, blank=True, null=True)
	Delegate_10_Committee = models.CharField(max_length=120, blank=True, null=True, choices=COMMITTEE)

	Faculty_Advisor_1_Name = models.CharField(max_length=120, blank=True, null=True)
	Faculty_Advisor_2_Name = models.CharField(max_length=120, blank=True, null=True)
	Faculty_Advisor_3_Name = models.CharField(max_length=120, blank=True, null=True)
	Faculty_Advisor_4_Name = models.CharField(max_length=120, blank=True, null=True)
	Faculty_Advisor_5_Name = models.CharField(max_length=120, blank=True, null=True)
	def __unicode__(self):
		return self.Name_of_School

class PositionPaper(models.Model):
	Name_of_School = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter the name of your institution. Make sure it is spelt exactly how it is specified on the dashboard. Do not put accents in the name or the submission will not work.</small></small></em>")
	Your_Name = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter your full name</small></small></em>")
	Your_Committee = models.CharField(max_length=120, blank=False, null=True, choices=COMMITTEE, help_text="<em><small><small>Please enter the name of your committee</small></small></em>")
	Your_Country = models.CharField(max_length=120, blank=False, null=True, help_text="<em><small><small>Please enter the name of your country</small></small></em>")
	file = models.FileField(null=True, blank=False)
	def __unicode__(self):
		return self.Name_of_School

class CountryAssignment(models.Model):
	Faculty_Advisor_Email = models.EmailField()
	Country_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_1_Committee_9 = models.CharField(max_length=220, blank=True, null=True)
	
	Country_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_2_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_3_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_4_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_5_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_6_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_7_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_8_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_9 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_9_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_10 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_10_Committee_9 = models.CharField(max_length=220, blank=True, null=True)
	Country_11 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_11_Committee_9 = models.CharField(max_length=220, blank=True, null=True)
	Country_12 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_12_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_13 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_13_Committee_9 = models.CharField(max_length=220, blank=True, null=True)

	Country_14 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_14_Committee_9 = models.CharField(max_length=220, blank=True, null=True)
	Country_15 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_1 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_2 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_3 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_4 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_5 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_6 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_7 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_8 = models.CharField(max_length=220, blank=True, null=True)
	Country_15_Committee_9 = models.CharField(max_length=220, blank=True, null=True)
