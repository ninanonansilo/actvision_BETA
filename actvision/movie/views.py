from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from imgn.media_json import *
# Create your views here.
def movie(request):
    play_list = directory_list()
    print("현재 등록된 재생목록->")
    print(play_list)  # 저장된 이미지 리스트

    list_dict = {
        'play_list': play_list,
    }
    context = json.dumps(list_dict)
    return render(request, 'mov.html', {'context': context})

@csrf_exempt
def upload_list(request):  # 재생목록 추가 ( GCP에 해당하는 이름의 디렉토리를 만듬)
    if request.method == 'POST':
        if request.is_ajax():
            print(request.POST['list'])    # 리스트 이름
            input = request.POST['list']
            #list_name = recursion_check(input) # 중복을 처리한 이름
            #print(list_name)
            list_name = input # 임시방편
            # -- 업로드 , 이런식으로 하면 오류 없이 디렉토리 생성가능
            UPLOAD("ynu-mcl-act", 'test' , user_id + "/PLAY_LIST/" + str(list_name) + "/")
            # -- 맨 첫 파일은 만든 시간으로 하나 만들어서 UI에 띄우는 용도로 사용
            now_kst = time_now()  # 현재시간 받아옴
            UPLOAD("ynu-mcl-act", 'test', user_id + "/PLAY_LIST/" + str(list_name) + now_kst.strftime("/%Y%m%d%H%M%S"))

            return redirect('movie.html')
        else:
            print("ajax 통신 실패!")
            return redirect('movie.html')
    else:
        print("POST 호출 실패!")
        return redirect('movie.html')


def recursion_check(input_value): # 중복체크
    input_value = input_value + "/"
    overlab_check = {} # dictionary
    string_list = play_list_in_bucket("ynu-mcl-act")
    print('현재 리스트에는 다음과 같이 있습니다 : ', string_list)
    string_list_copy = string_list
    for i in range(len(string_list)):
        if(len(string_list[i]) >= 4):
            if((string_list[i][-4:-3] == '(') and (string_list[i][-2:-1] == ')')):
                string_list_copy[i] = string_list[i][:-4]
        else:
            string_list_copy[i] = string_list[i][:-1]
    # print(string_list_copy)
    for i in range(len(string_list_copy)):
        try:
            overlab_check[string_list_copy[i]] += 1
        except:
            overlab_check[string_list_copy[i]] = 0
    print('위의 리스트를 중복처리 하고 개수 체크 : ', overlab_check)
    try:
        overlab_check[input_value] += 1
        ans = input_value +'(' + str(overlab_check[input_value]) + ')'
        print(ans)
        return ans
    except:
        overlab_check[input_value] = 0
        print(input_value)
        return input_value


def directory_list():   # 디렉토리가 '/'로 끝나는 특징을 사용해 디렉토리 이름만 추출
    play_list_name = play_list_in_bucket("ynu-mcl-act")  # 중복 확인을 위해 PLAY_LIST 하위 이름들의 배열
    list_name = []
    for i in range(len(play_list_name)):
        if play_list_name[i][-1:] == '/':
            list_name.append(play_list_name[i][:-1])
    return list_name


