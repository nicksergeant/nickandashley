from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.mail import EmailMessage

from guests.forms import *
from guests.models import RSVP

def rsvp(request):

    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            if form.cleaned_data['number_of_guests'] is None:
                rsvp.number_of_guests = 0
            rsvp.save()

            rsvps = RSVP.objects.all()
            total = 0

            for rsvpi in rsvps:
                total = total + int(rsvpi.number_of_guests)

            msg = EmailMessage('New wedding RSVP from %s %s' % (form.cleaned_data['guest_1_first_name'], form.cleaned_data['guest_1_last_name']), '%s %s just RSVPd for the wedding. View it here: http://nickandashley.org/admin/guests/rsvp/<br><br>So far, there have been %d guests who have RSVPd.' % (form.cleaned_data['guest_1_first_name'], form.cleaned_data['guest_1_last_name'], total), 'NickandAshley.org' + ' <sites@nicksergeant.com>', ['nick@nick.sg', 'ashley@ash-taylor.com'])
            msg.content_subtype = "html"
            #msg.send()
            return HttpResponseRedirect('/rsvp/thanks/')
        form = form
    else:
        form = RSVPForm()
    return render_to_response('rsvp.html', locals(), context_instance=RequestContext(request))

def rsvp_total_csv(request):
    rsvps = RSVP.objects.filter(attending='Y')

    table_1 = []
    table_2 = []
    table_3 = []
    table_4 = []
    table_5 = []
    table_6 = []
    table_7 = []
    table_8 = []
    table_9 = []
    table_10 = []
    table_11 = []
    table_12 = []
    table_13 = []
    table_14 = []

    for r in rsvps:

        r.guest_1_first_name = r.guest_1_first_name.strip(' ')
        r.guest_1_last_name = r.guest_1_last_name.strip(' ')
        r.guest_2_first_name = r.guest_2_first_name.strip(' ')
        r.guest_2_last_name = r.guest_2_last_name.strip(' ')
        r.guest_3_first_name = r.guest_3_first_name.strip(' ')
        r.guest_3_last_name = r.guest_3_last_name.strip(' ')
        r.guest_4_first_name = r.guest_4_first_name.strip(' ')
        r.guest_4_last_name = r.guest_4_last_name.strip(' ')

        if r.guest_1_first_name != '':
            r.guest_1_meal_choice = get_meal(r.guest_1_meal)

        if r.guest_2_first_name != '':
            r.guest_2_meal_choice = get_meal(r.guest_2_meal)
        
        if r.guest_3_first_name != '':
            r.guest_3_meal_choice = get_meal(r.guest_3_meal)

        if r.guest_4_first_name != '':
            r.guest_4_meal_choice = get_meal(r.guest_4_meal)

        if r.guest_1_table == None:
            r.guest_1_table = ''
        else:
            table = int(r.guest_1_table)
            name = r.guest_1_first_name + ' ' + r.guest_1_last_name + ' (' + r.guest_1_meal_choice + ')'

            if table == 1:
                table_1.append(name)
            if table == 2:
                table_2.append(name)
            if table == 3:
                table_3.append(name)
            if table == 4:
                table_4.append(name)
            if table == 5:
                table_5.append(name)
            if table == 6:
                table_6.append(name)
            if table == 7:
                table_7.append(name)
            if table == 8:
                table_8.append(name)
            if table == 9:
                table_9.append(name)
            if table == 10:
                table_10.append(name)
            if table == 11:
                table_11.append(name)
            if table == 12:
                table_12.append(name)
            if table == 13:
                table_13.append(name)
            if table == 14:
                table_14.append(name)
            
        if r.guest_2_table == None:
            r.guest_2_table = ''
        else:
            table = int(r.guest_2_table)
            name = r.guest_2_first_name + ' ' + r.guest_2_last_name + ' (' + r.guest_2_meal_choice + ')'

            if table == 1:
                table_1.append(name)
            if table == 2:
                table_2.append(name)
            if table == 3:
                table_3.append(name)
            if table == 4:
                table_4.append(name)
            if table == 5:
                table_5.append(name)
            if table == 6:
                table_6.append(name)
            if table == 7:
                table_7.append(name)
            if table == 8:
                table_8.append(name)
            if table == 9:
                table_9.append(name)
            if table == 10:
                table_10.append(name)
            if table == 11:
                table_11.append(name)
            if table == 12:
                table_12.append(name)
            if table == 13:
                table_13.append(name)
            if table == 14:
                table_14.append(name)

        if r.guest_3_table == None:
            r.guest_3_table = ''
        else:
            table = int(r.guest_3_table)
            name = r.guest_3_first_name + ' ' + r.guest_3_last_name + ' (' + r.guest_3_meal_choice + ')'

            if table == 1:
                table_1.append(name)
            if table == 2:
                table_2.append(name)
            if table == 3:
                table_3.append(name)
            if table == 4:
                table_4.append(name)
            if table == 5:
                table_5.append(name)
            if table == 6:
                table_6.append(name)
            if table == 7:
                table_7.append(name)
            if table == 8:
                table_8.append(name)
            if table == 9:
                table_9.append(name)
            if table == 10:
                table_10.append(name)
            if table == 11:
                table_11.append(name)
            if table == 12:
                table_12.append(name)
            if table == 13:
                table_13.append(name)
            if table == 14:
                table_14.append(name)

        if r.guest_4_table == None:
            r.guest_4_table = ''
        else:
            table = int(r.guest_4_table)
            name = r.guest_4_first_name + ' ' + r.guest_4_last_name + ' (' + r.guest_4_meal_choice + ')'

            if table == 1:
                table_1.append(name)
            if table == 2:
                table_2.append(name)
            if table == 3:
                table_3.append(name)
            if table == 4:
                table_4.append(name)
            if table == 5:
                table_5.append(name)
            if table == 6:
                table_6.append(name)
            if table == 7:
                table_7.append(name)
            if table == 8:
                table_8.append(name)
            if table == 9:
                table_9.append(name)
            if table == 10:
                table_10.append(name)
            if table == 11:
                table_11.append(name)
            if table == 12:
                table_12.append(name)
            if table == 13:
                table_13.append(name)
            if table == 14:
                table_14.append(name)

    seated = len(table_1) + len(table_2) + len(table_3) + len(table_4) + len(table_5) + len(table_6) + len(table_7) + len(table_8) + len(table_9) + len(table_10) + len(table_11) + len(table_12) + len(table_13) + len(table_14)

    return render_to_response('rsvp-total.csv', locals(), context_instance=RequestContext(request))

def get_meal(guest_meal):
    if guest_meal == 'P':
        return 'B'
    elif guest_meal == 'C':
        return 'C'
    elif guest_meal == 'S':
        return 'H'
    elif guest_meal == 'A':
        return 'P'
    elif guest_meal == 'K':
        return 'F'
    else:
        return ''

def rsvp_total(request):
    rsvps = RSVP.objects.filter(attending='Y')
    (prime_rib, chicken, haddock, pasta, chicken_fingers) = (0,) * 5
    total = 0
    count = 1
    over_21 = 0

    for r in rsvps:
        total = total + r.number_of_guests

        if r.guest_1_first_name != '':
            r.guest_1 = count
            count = count + 1

            if r.guest_1_over_21:
                over_21 = over_21 + 1

        if r.guest_2_first_name != '':
            r.guest_2 = count
            count = count + 1

            if r.guest_2_over_21:
                over_21 = over_21 + 1

        if r.guest_3_first_name != '':
            r.guest_3 = count
            count = count + 1

            if r.guest_3_over_21:
                over_21 = over_21 + 1

        if r.guest_4_first_name != '':
            r.guest_4 = count
            count = count + 1

            if r.guest_4_over_21:
                over_21 = over_21 + 1

        for meal in [r.guest_1_meal, r.guest_2_meal, r.guest_3_meal, r.guest_4_meal]:
            if meal == 'P':
                prime_rib = prime_rib + 1
            elif meal == 'C':
                chicken = chicken + 1
            elif meal == 'S':
                haddock = haddock + 1
            elif meal == 'A':
                pasta = pasta + 1
            elif meal == 'K':
                chicken_fingers = chicken_fingers + 1

    return render_to_response('rsvp-total.html', locals(), context_instance=RequestContext(request))
