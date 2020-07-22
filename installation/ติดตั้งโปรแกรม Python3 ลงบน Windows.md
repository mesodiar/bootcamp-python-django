## ติดตั้งโปรแกรม Python3 ลงบน Windows



1. เข้าเว็บ https://www.python.org/downloads/ เพื่อดาวน์โหลดไฟล์

   โดยให้คลิกปุ่ม Download Python 3.8.5

![Screen Shot 2563-07-21 at 15.30.26](/Users/mesodiar/Library/Application Support/typora-user-images/Screen Shot 2563-07-21 at 15.30.26.png)





2. เมื่อดาวน์โหลดเสร็จแล้ว ให้กด double click เพื่อทำการติดตั้ง

ขั้นตอนนี้สำคัญมาก **ให้กดติ๊กถูก** ที่ **Add Python 3.8 to PATH** ด้วย

และกด Install Now

![Screen Shot 2563-07-21 at 14.33.51](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 14.33.51.png)





3. เช็คว่า Python ได้ถูกติดตั้งแล้วหรือไม่

   ให้กดปุ่ม windows แล้ว search หาโปรแกรมที่ชื่อ Command Prompt แล้วกดเปิด program

![Screen Shot 2563-07-21 at 14.37.42](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 14.37.42.png)



4. ให้ลองพิมพ์ว่า python ดู หากว่า python ได้รับการติดตั้งแล้วจะขึ้นตามดังรูป

![Screen Shot 2563-07-21 at 14.37.53](/Users/mesodiar/Desktop/Screen Shot 2563-07-21 at 14.37.53.png)





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

![Screen Shot 2563-07-21 at 15.49.30](/Users/mesodiar/Library/Application Support/typora-user-images/Screen Shot 2563-07-21 at 15.49.30.png)



