기말프로젝트 준비
==================

### 1. 게임의 소개
* __제목 - 동방프로젝트 [탄막슈팅게임]__      
![팬메이드_동방프로젝트](https://i.ytimg.com/vi/85bE4NlzrLE/hqdefault.jpg)     
     
+ *게임의 목적* - 단순히 캐릭터를 움직여 다양한 패턴의탄막을 피하며 보스를 공격하여 hp를 0으로 만든다.
+ *게임 방법* - 플레이어는 방향키로 조작, z키로 공격, shift키를 누른채로 이동하면 느리게 이동이 가능하다.       

-------------------------------------------------------
### 2. GameState (Scene) 의 수 및 각각의 이름    
![Diagram](https://user-images.githubusercontent.com/71130227/94275907-7c08bc00-ff82-11ea-8a1c-8e37a7f57870.png)       

- - - 
### 3. State별 설명
1. __타이틀화면__ - 게임시작시 처음나오는 게임관련된 배경에 게임시작, 옵션, 게임설명과 같은 선택지가 있는 화면
    * 객체 목록 : 각각의 선택지 object와 배경이미지 
    + 처리할 이벤트 : 아래 위 키보드로 선택지 이동과 공격키(z)로 선택
    - 다른 State이동 조건 : 선택지를 선택하면 해당하는 state로 이동
    
2. __게임 옵션__ - 음량조절등 환경설정이 가능한 화면
    * 객체 목록 : 환경설정을 할 수있는 객체
    + 처리할 이벤트 : 상하 키보드로 선택지 이동 공격키로 선택    
    뒤로가기 키로 취소    
    좌우키로 크기조절
    - State 이동 조건 : 선택하지 않은 상태에서 뒤로가기 키를 누르면 타이틀 화면으로 다시 이동

3. __캐릭터 / 난이도 선택__ - 캐릭터나 난이도를 선택하는 화면
    * 객체 목록 : 난이도나 캐릭터 선택을 위한 객체
    + 처리할 이벤트 : 게임 옵션과 동일
    - State 이동 조건 : 아무것도 선택하지 않은 상태에서 다시 뒤로가기를 누르면 타이틀화면으로 이동,    
                        난이도와 캐릭터 선택을 다 했다면 게임화면으로 이동
                        
4. __게임 화면__ - 게임을 진행하는 화면, 적과 플레이어 캐릭터가 있고 탄막을 주고받으며 몇가지 UI가 있다.
    * 객체 목록 : 플레이어, 적, UI, 탄막
    + 처리할 이벤트 : 상하좌우로 플레이어 이동    
    공격키로 공격 [탄막발사]    
    메뉴키로 일시정지    
    - State 이동 조건 : 게임 중 일시정지 키를 누르면 메뉴화면으로 이동    
    게임을 끝까지 하면 Score 화면으로 이동
    
5. __스코어 화면__ - 게임동안 총 몇번을 피격했는지 여부로 Score를 알려주는 화면
    * 객체 목록 : Score 출력을 위한 UI 객체
    + 처리할 이벤트 : 공격또는 뒤로가기 키 
    - State 이동 조건 : 스코어 출력이 끝나고 공격키또는 뒤로가기키를 누르면 타이틀 화면으로 이동
    
6. __일시정지 화면__ - 게임을 일시정지 시킬때 출력되는 화면
    * 객체 목록 : 선택지 UI
    + 처리할 이벤트 : 상하키로 선택지 이동     
    공격키로 선택 
    - State 이동 조건 : 선택지에 따라 게임으로 돌아가거나, 타이틀로 돌아가거나, 옵션이나 게임설명창에 다녀옴     
    _다이어 그램에서 잘못 그린것 -> 타이틀화면에서 일시정지 화면으로 돌아가는건 안됨_
    
7. __게임 설명__ - 단순히 게임방법을 설명하는 화면
    * 객체 목록 : 설명문 출력을 위한 객체
    + 처리할 이벤트 : 뒤로가기 키
    - State 이동 조건 : 뒤로가기 키를 입력하면 전에있던 State로 이동함.    
    
- - -
    
### 4. 필요한 기술    
    * _다른 과목에서 배운 기술_ - 탄막패턴을 만들기위한 수학적 지식과 알고리즘    
    + _ 이 과목에서 배울 것으로 기대되는 기술_ - 객체와 모듈들을 효율적으로 나누고 관리하는법, 캐릭터 애니메이션, 배경음악이나 효과음 넣기,
    투명도를 조절해서 이미지 삽입, 탄막의 충돌처리    
    = _다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술_ - 탄막을 사용하면서 객체가 많이 생길것이라 예상되다보니 객체 생성과 삭제를 적절히 하는 방법.
    프로그래밍적으로 메모리를 잘 관리하는법을 배우고 싶습니다. 
