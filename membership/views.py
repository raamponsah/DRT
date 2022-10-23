import json

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from membership.forms import MembershipForm, MemberReligiousCVForm
from membership.models import Member, MemberReligiousCV

# Create your views here.
from utilities.send_sms import send_sms


def member(request, pk):
    found_member = Member.objects.select_related('member_ccv').get(pk=pk)
    # print(found_member.member_ccv.baptism_location)
    # print(found_member.member_ccv.baptism_location)
    context = {'member': found_member}
    return render(request, 'membership/member_profile.html', context)


def members(request):
    all_members = Member.objects.all()
    context = {'members': all_members, 'table_name': 'Membership Data',
               'dbtn': 'membership-download'}
    return render(request, 'membership/members.html', context)


def delete_member(request, pk):
    found_member = Member.objects.get(pk=pk)
    if request.method == 'POST':
        found_member.delete()
        return redirect('members')


def add_member(request):
    membership_form = MembershipForm()
    context = {'membership_form': membership_form, 'page_title': 'Add New Member'}

    if request.method == 'POST':
        membership_form = MembershipForm(request.POST, request.FILES)

        if membership_form.is_valid():
            new_member = membership_form.save()
            messages.success(request, f"Record saved successfully")

            send_sms(sendto=f'{new_member.primary_phone}',
                     message_content=f"Welcome {new_member.fullname}! You have been added to the church membership "
                                     f"successfully! We will be in touch. Stay blessed.")

            return redirect('add-religious-info', pk=new_member.pk)
        else:
            messages.error(request, f"Record saving unsuccessful")
            membership_form = MembershipForm(request.POST, request.FILES, )
            membership_form_errors = membership_form.errors.as_json()
            context['membership_form_errors'] = membership_form_errors
            context['membership_form'] = membership_form
            return render(request, 'membership/add_member.html', context)

    return render(request, 'membership/add_member.html', context)


def edit_member(request, pk):
    found_member = get_object_or_404(Member, pk=pk)
    membership_form = MembershipForm(instance=found_member)
    context = {'membership_form': membership_form, 'page_title': f"Edit {found_member}", 'member': found_member}

    if request.method == 'POST':
        membership_form = MembershipForm(request.POST, request.FILES, instance=found_member)
        if membership_form.is_valid():
            if request.FILES is None:
                request.FILES['profile_photo'] = 'default_profile_photo.jpeg'
                membership_form = MembershipForm(request.POST, request.FILES, instance=found_member)
            membership_form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('members')
        else:
            messages.error(request, f"Record saving unsuccessful")
            membership_form = MembershipForm(request.POST, request.FILES)
            membership_form_errors = membership_form.errors.as_json()
            context['membership_form_errors'] = membership_form_errors
            context['membership_form'] = membership_form
            return render(request, 'membership/edit_member.html', context)

    return render(request, 'membership/edit_member.html', context)


# membership religious methods
def add_religious_info(request, pk):
    found_member = get_object_or_404(Member, pk=pk)
    mcv = MemberReligiousCVForm(initial={'member': found_member})
    print(mcv)
    context = {'mcv_form': mcv, 'page_title': 'Dashboard', 'member': found_member}

    if request.method == 'POST':
        mcv = MemberReligiousCVForm(request.POST, initial={'member': found_member})
        if mcv.is_valid():

            # MemberReligiousCV(member=found_member, **mcv.cleaned_data)
            mcv.save()
            messages.success(request, f"Record saved successfully")
            return redirect('members')
        else:
            print(json.loads(mcv.errors.as_json()))

            messages.error(request, f"Record saving unsuccessful")
            mcv = MemberReligiousCVForm(request.POST)
            mcv_errors = json.loads(mcv.errors.as_json())
            context['mcv_errors'] = mcv_errors
            context['mcv_form'] = mcv
            return render(request, 'membership/add_mcv.html', context)

    return render(request, 'membership/add_mcv.html', context)


def update_religious_info(request, pk):
    found_member = get_object_or_404(Member, pk=pk)
    member_rcv = MemberReligiousCV.objects.get(member=found_member)
    mcv = MemberReligiousCVForm(instance=member_rcv)

    context = {'mcv_form': mcv, 'member': found_member}

    if request.method == 'POST':
        mcv = MemberReligiousCVForm(request.POST, instance=member_rcv)
        if mcv.is_valid():
            mcv.save()
            messages.success(request, f"Record saved successfully")
            return redirect('member', pk=found_member.pk)
        else:
            print(json.loads(mcv.errors.as_json()))

            messages.error(request, f"Record saving unsuccessful")
            mcv = MemberReligiousCVForm(request.POST)
            mcv_errors = json.loads(mcv.errors.as_json())
            context['mcv_errors'] = mcv_errors
            context['mcv_form'] = mcv
            return render(request, 'membership/edit_mcv.html', context)

    return render(request, 'membership/edit_mcv.html', context)