from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# ############################################# BSA ############################################### #

class first_year_first_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = First Year First Semester'
        verbose_name_plural = 'BSA = First Year First Semester'
    def __str__(self):
        return self.course_number

class first_year_second_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = First Year Second Semester'
        verbose_name_plural = 'BSA = First Year Second Semester'
    def __str__(self):
        return self.course_number
class first_year_summer_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = First Year Summer'
        verbose_name_plural = 'BSA = First Year Summer'
    def __str__(self):
        return self.course_number

class second_year_first_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Second Year First Semester'
        verbose_name_plural = 'BSA = Second Year First Semester'
    def __str__(self):
        return self.course_number

class second_year_second_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Second Year Second Semester'
        verbose_name_plural = 'BSA = Second Year Second Semester'
    def __str__(self):
        return self.course_number

class second_year_summer_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Second Year Summer'
        verbose_name_plural = 'BSA = Second Year Summer'
    def __str__(self):
        return self.course_number

class third_year_first_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Third Year First Semester'
        verbose_name_plural = 'BSA = Third Year First Semester'
    def __str__(self):
        return self.course_number

class third_year_second_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Third Year Second Semester'
        verbose_name_plural = 'BSA = Third Year Second Semester'
    def __str__(self):
        return self.course_number

class third_year_summer_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Third Year Summer'
        verbose_name_plural = 'BSA = Third Year Summer'
    def __str__(self):
        return self.course_number

class fourth_year_first_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Fourth Year First Semester'
        verbose_name_plural = 'BSA = Fourth Year First Semester'
    def __str__(self):
        return self.course_number

class fourth_year_second_semester_bsa(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSA = Fourth Year Second Semester'
        verbose_name_plural = 'BSA = Fourth Year Second Semester'
    def __str__(self):
        return self.course_number
# ########################################### MATH MAJOR ############################################## #

class first_year_first_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = First Year First Semester'
        verbose_name_plural = 'LAED-MATH = First Year First Semester'
    def __str__(self):
        return self.course_number
class first_year_second_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = First Year Second Semester'
        verbose_name_plural = 'LAED-MATH = First Year Second Semester'
    def __str__(self):
        return self.course_number
class second_year_first_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Second Year First Semester'
        verbose_name_plural = 'LAED-MATH = Second Year First Semester'
    def __str__(self):
        return self.course_number
class second_year_second_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Second Year Second Semester'
        verbose_name_plural = 'LAED-MATH = Second Year Second Semester'
    def __str__(self):
        return self.course_number
class third_year_first_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Third Year First Semester'
        verbose_name_plural = 'LAED-MATH = Third Year First Semester'
    def __str__(self):
        return self.course_number
class third_year_second_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Third Year Second Semester'
        verbose_name_plural = 'LAED-MATH = Third Year Second Semester'
    def __str__(self):
        return self.course_number
class fourth_year_first_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Fourth Year First Semester'
        verbose_name_plural = 'LAED-MATH = Fourth Year First Semester'
    def __str__(self):
        return self.course_number
class fourth_year_second_semester_math(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'LAED-MATH = Fourth Year Second Semester'
        verbose_name_plural = 'LAED-MATH = Fourth Year Second Semester'
    def __str__(self):
        return self.course_number
# ########################################## BSN ####################################################### #
class first_year_first_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = First Year First Semester'
        verbose_name_plural = 'BSN = First Year First Semester'
    def __str__(self):
        return self.course_number
class first_year_second_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = First Year Second Semester'
        verbose_name_plural = 'BSN = First Year Second Semester'
    def __str__(self):
        return self.course_number
class first_year_summer_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = First Year Summer'
        verbose_name_plural = 'BSN = First Year Summer'
    def __str__(self):
        return self.course_number
class second_year_first_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Second Year First Semester'
        verbose_name_plural = 'BSN = Second Year First Semester'
    def __str__(self):
        return self.course_number
class second_year_second_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Second Year Second Semester'
        verbose_name_plural = 'BSN = Second Year Second Semester'
    def __str__(self):
        return self.course_number
class second_year_summer_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Second Year Summer'
        verbose_name_plural = 'BSN = Second Year Summer'
    def __str__(self):
        return self.course_number
class third_year_first_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=500)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Third Year First Semester'
        verbose_name_plural = 'BSN = Third Year First Semester'
    def __str__(self):
        return self.course_number
class third_year_second_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=500)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Third Year Second Semester'
        verbose_name_plural = 'BSN = Third Year Second Semester'
    def __str__(self):
        return self.course_number
class fourth_year_first_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=500)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Fourth Year First Semester'
        verbose_name_plural = 'BSN = Fourth Year First Semester'
    def __str__(self):
        return self.course_number
class fourth_year_second_semester_bsn(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    lecture             =   models.CharField(max_length=100)
    lab                 =   models.CharField(max_length=100, blank=True)
    requisite           =   models.CharField(max_length=100, blank=True)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSN = Fourth Year Second Semester'
        verbose_name_plural = 'BSN = Fourth Year Second Semester'
    def __str__(self):
        return self.course_number

# ############################################ BSBA ################################################ #
class first_year_first_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = First Year First Semester'
        verbose_name_plural = 'BSBA = First Year First Semester'

class first_year_second_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = First Year Second Semester'
        verbose_name_plural = 'BSBA = First Year Second Semester'

class second_year_first_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Second Year First Semester'
        verbose_name_plural = 'BSBA = Second Year First Semester'

class second_year_second_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Second Year Second Semester'
        verbose_name_plural = 'BSBA = Second Year Second Semester'

class third_year_first_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Third Year First Semester'
        verbose_name_plural = 'BSBA = Third Year First Semester'

class third_year_second_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Third Year Second Semester'
        verbose_name_plural = 'BSBA = Third Year Second Semester'

class fourth_year_first_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Fourth Year First Semester'
        verbose_name_plural = 'BSBA = Fourth Year First Semester'

class fourth_year_second_semester_bsba(models.Model):
    course_number       =   models.CharField(max_length=100)
    descriptive_title   =   models.CharField(max_length=100)
    requisite           =   models.CharField(max_length=100, blank=True)
    lab                 =   models.CharField(max_length=100, blank=True)
    lecture             =   models.CharField(max_length=100)
    no_of_units         =   models.CharField(max_length=100)
    class Meta:
        verbose_name = 'BSBA = Fourth Year Second Semester'
        verbose_name_plural = 'BSBA = Fourth Year Second Semester'

# ##############################################################
class ForSMS(models.Model):
    name                =   models.CharField(max_length=50)
    number              =   models.CharField(max_length=10)