from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path("font")
LabelBase.register(DEFAULT_FONT,"MSGOTHIC.TTC")

KV_CODE='''
TextWidget:

<TextWidget>:
 BoxLayout:
  orientation:"vertical"
  size:root.size
  Label:
   #text:"Enter the characters you want to convert"
   text:"変換したい値を入力"
   size_hint_y:0.2
   text_size: self.size
   halign: 'center'
   valign: 'middle'

  TextInput:
   size_hint_y:0.1
   id:text_input

  Label:
   id:label1
   text:root.text
   size_hint_y:0.2
   text_size: self.size
   halign: 'center'
   valign: 'middle'

  BoxLayout:
   orientation:"vertical"
   Button:
    id:button2
    text:"2進数を10進数に"
    #text:"2to10"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked2()
   Button:
    id:button3
    text:"2進数を16進数に"
    #text:"2to16"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked3()
   Button:
    id:button4
    text:"10進数を2進数に"
    #text:"10to2"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked4()
   Button:
    id:button5
    text:"10進数を16進数に"
    #text:"10to16"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked5()
   Button:
    id:button6
    text:"16進数を2進数に"
    #text:"16to2"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked6()
   Button:
    id:button7
    text:"16進数を10進数に"
    #text:"16to10"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked7()
   Button:
    text:"決定"
    text:"Enter"
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    on_press:root.buttonClicked()
'''

def one():
    global sixteen_str_list_big,sixteen_str_list_small
    sixteen_str_list_big=["A","B","C","D","E","F"]
    sixteen_str_list_small=["a","b","c","d","e","f"]

class TextWidget(Widget):
    text=StringProperty()
    def __init__(self,**kwargs):
        super(TextWidget,self).__init__(**kwargs)
        self.text="変換結果:"+"\n"+"モード:"
        #self.text="conversion result:"+"\n"+"Mode:"
    def buttonClicked(self):
        def main_update():
            global answer
            def sixteen_to_ten(n):
                try:
                    answer=0
                    n_list=[]
                    n_list=list(n)
                    for i in range(len(n_list)):
                        for x in range(6):
                            sixteen_str=x+10
                            if n_list[i]==sixteen_str_list_big[x]:
                                n_list[i]=sixteen_str
                            elif n_list[i]==sixteen_str_list_small[x]:
                                n_list[i]=sixteen_str
                        n_list[i]=int(n_list[i])
                    n_list.reverse()
                    tmp=1
                    for i in range(len(n_list)):
                        if i==0:
                            answer=n_list[i]
                        else:
                            tmp=16*tmp
                            answer=answer+n_list[i]*tmp
                    return answer
                except Exception as e:
                    pass

            def two_to_ten(n):
                #2を10へ
                try:
                    answer=0
                    n_list=[]
                    n_list=list(n)
                    n_list = [int(i) for i in list(n)]
                    n_len=len(n_list)
                    loop=1
                    while n_len>0:
                        n_len=n_len-1
                        if n_list[n_len]==1:
                            answer=loop+answer
                        elif n_list[n_len]==0:
                            pass
                        else:
                            self.text="Input Error"+"\n"+"A value other than 0 and 1 is entered"
                        loop=loop*2
                    return answer
                except Exception as e:
                    pass

            def ten_to_sixteen(n):
                #10を16へ
                try:
                    answer=""
                    n=int(n)
                    n_list=[]
                    if n<16:
                        n_list.append(n)
                        for i in range(len(n_list)):
                            for x in range(6):
                                sixteen_str=x+10
                                if n_list[i]==sixteen_str:
                                    n_list[i]=sixteen_str_list_big[x]
                        answer="".join(str(s) for s in n_list)
                    else:
                        while n>=16:
                            n1=int(n/16)
                            n_list.append(n-(n1*16))
                            n=n1
                        n_list.append(n1)
                        n_list.reverse()
                        for i in range(len(n_list)):
                            for x in range(6):
                                sixteen_str=x+10
                                if n_list[i]==sixteen_str:
                                    n_list[i]=sixteen_str_list_big[x]
                        answer="".join(str(s) for s in n_list)
                    return answer
                except Exception as e:
                    pass
            def ten_to_two(n):
                #10を2へ
                try:
                    n=int(n)
                    n_list=[]
                    while n>1:
                        n1=int(n/2)
                        n_list.append(n-(n1*2))
                        n=n1
                    n_list.append(n1)
                    n_list.reverse()
                    answer="".join(str(s) for s in n_list)
                    return answer
                except Exception as e:
                    pass

            #if re_combo=="2to10":
            if re_combo=="2進数を10進数に":
                answer=two_to_ten(before)
            #elif re_combo=="2to16":
            elif re_combo=="2進数を16進数に":
                answer=two_to_ten(before)
                answer=ten_to_sixteen(answer)
            #elif re_combo=="10to2":
            elif re_combo=="10進数を2進数に":
                answer=ten_to_two(before)
            #elif re_combo=="10to16":
            elif re_combo=="10進数を16進数に":
                answer=ten_to_sixteen(before)
            #elif re_combo=="16to2":
            elif re_combo=="16進数を2進数に":
                answer=sixteen_to_ten(before)
                answer=ten_to_two(answer)
            #elif re_combo=="16to10":
            elif re_combo=="16進数を10進数に":
                answer=sixteen_to_ten(before)
        before=self.ids.text_input.text
        main_update()
        self.text="変換結果:"+str(answer)+"\n"+"モード:"+str(re_combo)
        #self.text="conversion result:"+str(answer)+"\n"+"Mode:"+str(re_combo)
    def buttonClicked2(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="2to10"
        re_combo="2進数を10進数に"
        self.text=nowmode()
    def buttonClicked3(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="2to16"
        re_combo="2進数を16進数に"
        self.text=nowmode()
    def buttonClicked4(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="10to2"
        re_combo="10進数を2進数に"
        self.text=nowmode()
    def buttonClicked5(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="10to16"
        re_combo="10進数を16進数に"
        self.text=nowmode()
    def buttonClicked6(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="16to2"
        re_combo="16進数を2進数に"
        self.text=nowmode()
    def buttonClicked7(self):
        global re_combo
        def nowmode():
            temp="変換結果:"+"\n"+"モード:"+str(re_combo)
            #temp="conversion result:"+"\n"+"Mode:"+str(re_combo)
            return temp
        #re_combo="16to10"
        re_combo="16進数を10進数に"
        self.text=nowmode()
class RadixApp(App):
    def __init__(self, **kwargs):
        super(RadixApp,self).__init__(**kwargs)
        self.title=("Radix Conversion")
    def build(self):
        Builder.load_string(KV_CODE)
        return TextWidget()

if __name__=='__main__':
    one()
    RadixApp().run()