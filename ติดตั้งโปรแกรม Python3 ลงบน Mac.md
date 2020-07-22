## ติดตั้งโปรแกรม Python3 ลงบน Mac

1. ให้เปิดโปรแกรม terminal ใน mac ขึ้นมา (หากมีโปรแกรม iTerm ก็ให้เปิด iTerm แทนได้)

   

![Screen Shot 2563-07-22 at 20.48.27](/Users/mesodiar/Desktop/Screen Shot 2563-07-22 at 20.48.27.png)



2. เราจะ install  'Homebrew' กัน หากมีในเครื่องแล้วให้ข้ามขั้นตอนนี้ได้เลย

   ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```

   

3. คราวนี้เราจะ install python3 กัน ให้รันคำสั่ง

   ```
   brew install python
   ```

   

   4. พอติดตั้งเสร็จแล้ว ให้ลองรัน

   ```
   python3
   ```

   ผลที่ได้จะเป็นดังรูป

   ![Screen Shot 2563-07-22 at 20.53.20](/Users/mesodiar/Library/Application Support/typora-user-images/Screen Shot 2563-07-22 at 20.53.20.png)

   (อย่าลืม exit() เพื่อออก )

5. เมื่อเราได้ทำการติดตั้ง python3 บนเครื่องแล้ว เราต้องเช็คให้แน่ใจว่าทุกครั้งที่เรารัน python เครื่องจะรู้ว่าเราใช้ python3 หรือไม่

   เพราะ mac จะมีการติดตั้ง python เวอร์ชั่น 2.7 มาให้โดยอัตโนมัติ

   

   เราจะลองเช็คดูจากการรัน

   ```
   python --version
   ```

   

![Screen Shot 2563-07-22 at 21.03.11](/Users/mesodiar/Desktop/Screen Shot 2563-07-22 at 21.03.11.png)

นั่นแสดงว่า ทุกครั้งที่มีการเรียกคำสั่ง python เครื่องจะใช้ python2.7 โดยอัติโนมัติ

ดังนั้นเราต้องแก้ให้เครื่องเลือก python ให้ถูกเวอร์ชั่น



ให้เรารัน

```
open ~/.zshrc
```



เพื่อเปิดไฟล์ .zshrc และเติม

```
alias python='python3'
```



เข้าไปในด้านล่างของไฟล์ไฟล์ และ ctrl+s เพื่อ save และปิดไฟล์



6. ปิดและเปิด terminal ใหม่และให้ลองรัน 

   ```
   python --version 
   ```

   

![Screen Shot 2563-07-22 at 21.17.40](/Users/mesodiar/Desktop/Screen Shot 2563-07-22 at 21.17.40.png)







## ใน VSCODE



เปิด VSCODE เพื่อติดตั้ง Python extension ใน VSCODE

1. เปิด VSCODE ขึ้นมา

( ตามรูป ) กดปุ่ม extensionsในตำแหน่งที่ 1 และเสิร์ชคำว่า Python และกด Install



![Screen Shot 2563-07-21 at 15.36.52](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 15.36.52.png)



2. ให้กด ctrl+shift+P จะมีหน้าต่าง popup มาดังรูป ให้พิมพ์คำว่า Python หากเห็นคำว่า **Python: Select interpreter**  ให้คลิกทันที



![Screen Shot 2563-07-21 at 15.39.22](/Users/mesodiar/Library/Application Support/typora-user-images/Screen Shot 2563-07-21 at 15.39.22.png)



เราจะเห็นว่ามี 2 ตัวเลือก ให้เราเลือกที่ Python 3.8.5 



![Screen Shot 2563-07-21 at 14.47.21](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 14.47.21.png)



3. ในแถบเมนู ในคลิกที่ Terminal > New Terminal

   เพื่อแสดงหน้าต่าง terminal ขึ้นมาในหน้าต่างขวาล่าง

![Screen Shot 2563-07-21 at 15.40.55](/Users/mesodiar/Library/Application Support/typora-user-images/Screen Shot 2563-07-21 at 15.40.55.png)



4. หากในแถบ terminal ด้านล่างขึ้นแล้ว ให้ลองพิมพ์คำว่า python ดู เพื่อเช็คว่าเราสามารถรันคำสั่ง python ใน terminal ของ VSCODE ได้ไหม

   หากไม่ได้ จะขึ้น error สีแดง  แสดงคำว่า

   ```
   The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
   ```

   ถ้าขึ้นตามนี้ แสดงว่าเราต้อง restart เครื่องใหม่ 



5. เมื่อเรา restart เครื่องใหม่แล้ว ให้ลองเข้า VSCODE อีกครั้ง และลองพิมพ์ python ใน terminal ดู

![Screen Shot 2563-07-21 at 15.27.02](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 15.27.02.png)

หากสำเร็จ จะขึ้นผลลัพท์ดังรูป





## ติดตั้ง Pipenv



1. ใน จอ terminal ใน VSCODE ให้เราพิมพ์ คำสั่ง

```
pip install pipenv

```

 และตามด้วย

```
python -m pipenv
```



ขั้นตอนนี้เป็นการติดตั้ง Pipenv หากลง Pipenv สำเร็จ จะเห็นผลลัพท์คล้ายรูปด้านล่าง


