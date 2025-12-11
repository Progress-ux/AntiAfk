import keyboard
from tkinter import Label
import threading
import random
import time

class Bober:
   def __init__(self, label: Label):
      self.keys = ['w', 'a', 's', 'd']
      self.running = False
      self.thread_worker = None
      self.status_label = label
   
   def press_key(self):
      """
      Автоматическое нажатие клавиш(w, a, s, d) в случайный период времени
      """
      while self.running:
         key = random.choice(self.keys)
         keyboard.press(key)
         time.sleep(random.uniform(0.5, 2.0))
         keyboard.release(key)
         time.sleep(random.uniform(0.3, 1.0))

   def toggle(self):
      """
      Переключает состояние программы
      """
      if not self.running:
         self.running = True
         self.status_label.config(text="Автоклик запущен")
         self.thread_worker = threading.Thread(target=self.press_key)
         self.thread_worker.start()
      else:
         self.running = False
         self.status_label.config(text="Автоклик остановлен")
