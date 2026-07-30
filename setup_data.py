import os
from torch.utils.data import DataLoader
from torchvision import datasets , transforms


def create_dataloader(train_dir,test_dir,transform,batch_size,num_workers = os.cpu_count()):

    train_data = datasets.ImageFolder(root = train_dir , transform = transform , target_transform = None)

    test_data = datasets.ImageFolder(root = test_dir , transform = transform , target_transform = None)

    class_names = train_data.classes

    train_dataloader = DataLoader(train_data , 32 , shuffle = True)
    test_dataloader = DataLoader(test_data , 32 , shuffle = False)


    return train_dataloader , test_dataloader , class_names