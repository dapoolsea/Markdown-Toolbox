def fileSizeNormalize(文件大小):
    if 文件大小 < 1024:
        return '%i' % 文件大小 + 'B'
    elif 1024 <= 文件大小 < (1024 ** 2):
        return '%.1f' % float(文件大小 / 1024) + 'KB'
    elif 1024 ** 2 <= 文件大小 < (1024 ** 3):
        return '%.1f' % float(文件大小 / (1024 ** 2)) + 'MB'
    elif 1024 ** 3 <= 文件大小 < (1024 ** 4):
        return '%.1f' % float(文件大小 / (1024 ** 3)) + 'GB'
    elif 1024 ** 4 <= 文件大小:
        return '%.1f' % float(文件大小 / (1024 ** 4)) + 'TB'
    else:
        return 文件大小