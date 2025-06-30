from django.db import models

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi convallis, erat nec laoreet tristique, metus urna ultrices mauris, nec elementum magna orci non neque. Nullam condimentum leo vitae eros porta malesuada. Nulla facilisi. Sed at quam eget metus pulvinar tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris lacinia, elit ac iaculis faucibus, arcu ante vestibulum lorem, nec efficitur elit sapien ac odio. Integer fermentum finibus mi, at convallis orci varius id. Nullam imperdiet lorem sed arcu finibus, non pretium erat cursus. Integer rutrum dui sit amet ante tincidunt, vitae tincidunt nulla vestibulum. Nullam sed vehicula velit. Cras nec congue purus. Pellentesque congue urna a sapien fermentum, a imperdiet ex finibus. Suspendisse varius sapien eget erat tempor, id eleifend nulla dapibus. Fusce lobortis, justo at volutpat posuere, sapien ante cursus nunc, at sodales nulla magna id enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Quisque viverra sapien vel purus rhoncus, nec gravida lorem tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed mollis lobortis enim. Curabitur nec turpis id elit imperdiet tempus. Phasellus et lacinia enim. Integer egestas, arcu in rhoncus feugiat, elit sapien porttitor risus, sed tincidunt ligula magna et mauris. Suspendisse ut felis erat. Nulla nec erat eu nisl condimentum faucibus. Nam nec sem neque. Aliquam dignissim lorem nec risus vehicula eleifend. Morbi id nisl eu nunc ultrices fringilla. Nunc luctus magna id lacus iaculis, nec imperdiet sapien blandit. Mauris ac leo ac nulla tincidunt posuere. Donec sollicitudin sapien quis velit posuere, a gravida risus imperdiet. Proin at turpis eu lectus pretium vestibulum. Donec non magna ac justo lacinia laoreet. Donec eget est at nulla congue rutrum a nec nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec nec purus efficitur, faucibus tellus eget, porttitor nunc. Cras quis erat sed odio ultricies tincidunt. Integer fermentum viverra bibendum. Sed at volutpat tortor, eget tincidunt lorem. Sed rhoncus malesuada magna, eget sagittis nunc posuere a. Integer tristique euismod diam, ut fringilla magna hendrerit non. Praesent vel nibh a elit laoreet faucibus. Integer gravida porta augue at porta. Curabitur eleifend nulla at lacus blandit, nec suscipit tortor pulvinar. Suspendisse non sapien at augue luctus imperdiet sed sed nisl. Etiam ac augue diam. Nunc eleifend dui eu orci feugiat, id facilisis nunc suscipit. Sed pulvinar risus sed lacus porta congue. Vestibulum efficitur augue in mi facilisis, id lobortis mi vehicula. Pellentesque vehicula fermentum ante ut fringilla. Nunc nec tincidunt magna. Quisque nec neque eu metus tristique consequat. Pellentesque sed odio finibus, feugiat sapien id, tempor libero. Curabitur sagittis nisl a rhoncus fermentum. Phasellus accumsan lacinia gravida."

class ProfilMadrasah(models.Model):
    nama = models.CharField(max_length=255, default='-')
    nsm = models.IntegerField(default=0)
    npsm = models.IntegerField(default=0)
    sk = models.CharField(max_length=255, default='-')
    akreditasi = models.CharField(max_length=255, default='-')
    alamat = models.CharField(max_length=255, default='-') 
    telepon = models.CharField(max_length=255, default='-') 
    faks = models.CharField(max_length=255, default='-')
    email = models.EmailField(default='service@example.com')
    website = models.URLField(default='https://example.com')
    status = models.CharField(max_length=255, default='-')
    lintang = models.CharField(max_length=255, default='-')
    bujur = models.CharField(max_length=255, default='-')
    kepsek = models.CharField(max_length=255, default='-')
    visi = models.TextField(default=lorem)
    sejarah = models.TextField(default=lorem)

class Misi(models.Model):
    profil = models.ForeignKey(ProfilMadrasah, on_delete=models.CASCADE, related_name='misi_list')
    isi = models.CharField(max_length=255)

    def __str__(self):
        return self.isi


class ProgramUnggulan(models.Model):
    nama_program = models.CharField(max_length=255)

class IsiProgram(models.Model):
    program = models.ForeignKey(ProgramUnggulan, on_delete=models.CASCADE, related_name='program_list')
    isi = models.CharField(max_length=255)
    
