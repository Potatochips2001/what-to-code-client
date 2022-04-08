#!/usr/bin/env python3
from array import array
import tkinter, requests, json, tkinter.messagebox

endpoint = 'https://what-to-code.com/api/ideas'

def sendIdea():
  global ui1, ui2, ui3
  ideaTitle = ui1.get(); ideaDescription = ui2.get(); ideaTags = ui3.get().split(' ')
  if len(ideaTitle) <= 5 or len(ideaTitle) >= 64:
    tkinter.messagebox.showwarning(title="dafuq", message="Title is either too small or large")
    return
  if len(ideaDescription) >= 512:
    tkinter.messagebox.showwarning(title="dafuq", message="Obsurdly long description")
    return
  if len(ideaTags) > 6:
    tkinter.messagebox.showwarning(title='Too many tags', message='Too many tags, max is 6')
    return
  tagsToSend = []
  for i in ideaTags:
    tagsToSend += [{"value": i}]
  packetText = json.dumps({
    "title": ideaTitle,
    "description": ideaDescription,
    "tags": tagsToSend
  })
  requests.post(endpoint, data=packetText)
  tkinter.messagebox.showinfo(message='Packet sent')

bgColor = '#111'

window = tkinter.Tk()
window.title("what-to-code - Client")
window.configure(background=bgColor)
window.geometry("400x150")

label1 = tkinter.Label(window, text="Title", background=bgColor).grid(row=0, column=0)
ui1 = tkinter.Entry(window, background='#222', width=20)
ui1.grid(row=0, column=1)

label2 = tkinter.Label(window, text="Description", background=bgColor).grid(row=1, column=0)
ui2 = tkinter.Entry(window, background='#222', width=20)
ui2.grid(row=1, column=1)

label3 = tkinter.Label(window, text="tags", background=bgColor).grid(row=2, column=0)
ui3 = tkinter.Entry(window, background='#222', width=20)
ui3.grid(row=2, column=1)

btn = tkinter.Button(text='Send packet',
foreground='#ccc',
background='#222',
width=10,
height=1,
command=sendIdea
).grid(row=3, column=1)


window.mainloop()
