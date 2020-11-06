#!/usr/bin/env python3
# Bashorun, E.

from collections import deque
import os


class BaseCrawl:
    def __init__(self):
        self.traversed = []
        self.global_queue = deque()
        self.metadata = {}

    def scan_dir(self, item):
        if os.path.isdir(item) is False:
            self.global_queue.append(item)
        else:
            with os.scandir(item) as it:
                for entry in it:
                    self.global_queue.append(entry)

    def get_metadata(self, item):
        # Get stat results
        try:
            stat_object = os.lstat(item)
        except FileNotFoundError:
            print('File not found!')
        else:
            inode_number = stat_object.st_ino
            hardlink_number = stat_object.st_nlink
            user_id = stat_object.st_uid
            group_id = stat_object.st_gid
            size = stat_object.st_size
            mode = stat_object.st_mode

            # Timestamps
            access_time = stat_object.st_atime
            modified_time = stat_object.st_mtime
            creation_time = stat_object.st_ctime

            full_pathname = item.path
            file_extension = os.path.splitext(item.name)
        
        '''
        logic to determine file type
        '''
        file_type = type_
        self.metadata = {
          'inode_number': inode_number, 'hardlink_number': hardlink_number,
          'user_id': user_id, 'group_id': group_id, 'size': size,
          'mode': mode, 'access_time': access_time,
          'modified_time': modified_time, 'creation_time': creation_time,
          'full_pathname': full_pathname, 'full_extension': file_extension,
          'file_type': type_
        }
        return self.metadata

    def scan_queue(self):
        index = 0
        while len(self.global_queue) != 0:
            item = self.global_queue[index]
            if item not in self.traversed:
                if os.path.isdir(item) is True:
                    self.scan_dir(item)
                    metadata = self.get_metadata(item)
                    self.traversed.append(item)
                else:
                    metadata = self.get_metadata(item)
            self.global_queue.popleft()
            print(metadata)
        return metadata


crawled = BaseCrawl()
crawled.scan_dir('/home/bashorun/Documents/bitcoin')
crawled.scan_queue()
