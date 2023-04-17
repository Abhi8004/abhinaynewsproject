from django.shortcuts import render

# Create your views here.
def Home_Page_view(request):
    return render(request,'testapp/home.html')

def movies_name_view(request):
    news1='devdas'
    news2='bagban'
    news3='bhagam bhag'
    news4='kantara'
    news5='circus'
    type='movies'
    my_dict={'news1':news1, 'news2':news2, 'news3':news3, 'news4':news4, 'news5':news5,'type':type}
    return render(request,'testapp/mnews.html',my_dict)

def sports_name_view(request):
    new1='kabaddi'
    new2='cricket'
    new3='vollyball'
    new4='football'
    new5='khokho'
    type='sports'
    my_dict={'new1':new1, 'new2':new2, 'new3':new3, 'new4':new4, 'new5':new5,'type':type}
    return render(request,'testapp/msports.html',my_dict)

def politics_name_view(request):
    nes1='modi'
    nes2='yogi'
    nes3='rahul'
    nes4='akhilesh'
    nes5='mayawati'
    type='politics'
    my_dict={'nes1':nes1, 'nes2':nes2, 'nes3':nes3, 'nes4':nes4, 'nes5':nes5,'type':type}
    return render(request,'testapp/mpolitics.html',my_dict)
