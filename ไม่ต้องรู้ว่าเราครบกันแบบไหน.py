import time

from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table

class Song:
  def __init__(self, songName: str, singer: str, lysics: tuple):
    self.songName = songName
    self.singer = singer
    self.lysics = lysics
    self.tiktokAccount = '<Khian Code Gun />'

  def display_lysics(self):
    table = Table(
      box = box.ROUNDED,
      width = 40,
      border_style = '#EB8222'
    )

    table.add_column(
      self.tiktokAccount, 
      justify='center',
      style = '')

    with Live(table, refresh_per_second=1):
      for line, delay in self.lysics: 
          table.add_row(line+'\n\n')
          time.sleep(delay)

    
    Console().print(
      '\n' + self.songName, 
      justify='center',
      style='italic #EB8222',
      width=40
    )
    Console().print(
      self.singer,
      justify='center',
      style='italic #F4F2EB',
      width=40
    )

Song2 = Song(
  songName= '-- ไม่ต้องรู้ว่าเราคบกันแบบไหน --',
  singer = 'Mind 4EVE x DGERRARD',
  lysics= (    
    ('ไม่ต้องรู้ว่าเราคบกันแบบไหน', 6),
    ('ไม่อาจหาคำคำไหนมาเพื่ออธิบาย', 8),
    ('ไม่ต้องรักเหมือนคนรักก็สุขหัวใจ', 6),
    ('เพียงแค่เราเข้าใจ เพียงแค่เราเข้าใจ', 5),
    ('ไม่ต้องรู้ว่าเราคบกันแบบไหน', 6),
    ('ไม่ต้องหาคำคำไหนมาเพื่ออธิบาย', 5),
    ('ไม่ต้องรักเหมือนคนรักก็สุขหัวใจ', 6),
    ('เพียงแค่เราเข้าใจ ก็เหนือคำอื่นใดในโลกนี้', 3),
  )
)

Song2.display_lysics()
