'''
Exited to do the first assignment.

This assignment is a simple one to make you ready for the followup assignments.

As a University, students details plays an important role. Instead of one person writing all your details, we intend to take it from you.

The Details are as follows:

Name:
Roll Number:
Branch:
Specialization:
Email ID:
Moodle ID:
GitHub ID:
Replit ID:
Semester:
Year(1-4):

Now your task is to put it in a dictionary like the below example

{
'name': {'first-name':'Rama', 'last-name':'Rao'},
'roll-number':'123456',
'branch':'CSE',
'specialization':'DS',
'email-id':'ramarao@gitam.in',
'moodle-id':'Rama Rao 123456',
'github-id':'ramarao',
'replit-id':'ramarao',
'semester':'2',
'year':'1'
}

In the above example we have a dictionary in a dictionary with `first-name` and `last-name` as the keys, It is must.

Now you are given the function like the below. Fill this function with the necessary code.

This function has to fill in the dictionary with the acquired input and return to the function caller which inturn will print the received dictionary.  

This function has to return a dictionary with all your details.
Make sure you fill in the right details.

'''

def my_details():
  """Return a dictionary with your details in the format as specified in the above instructions"""
  res={
'name': {'first-name':'Sahil', 'last-name':'Siddarth'},
'roll-number':'VU21EECE0100159',
'branch':'ECE',
'specialization':'AI and ML',
'email-id':'vvasamse@@gitam.in',
'moodle-id':'VASAMSETTI VIJAY VARDHAN Vu21eece0100159',
'github-id':'Vijay-159',
'replit-id':'@VASAMSETTI-VIJA',
'semester':'2',
'year':'1'
}
  return res

# now call your function
dt = my_details()
print(dt)


# Once you complete, no need to submit.
# The changes will be automatically saved.
# Wish you happy coding!!!
