import torchvision
import torch
import Training_Testing_Engine , utils  , setup_data , model_create
import os
from torchvision import transforms

def main():

    device = "cuda" if torch.cuda.is_available() else "cpu"

    transform = transforms.Compose([transforms.Resize(size=(128,128)) ,
                                transforms.RandomHorizontalFlip(p=0.5),
                                transforms.RandomRotation(15),
                                transforms.ColorJitter(brightness=0.15,
                                                       contrast = 0.15,
                                                       saturation=0.15),
                                 transforms.ToTensor() ,
                                   transforms.Normalize(mean=[0.659710109233, 0.617486357688, 0.586363255977],std=[0.27609637379, 0.2875597774982, 0.3020708858966])])

    train_dir = "data/garbage_classification_split/train"
    test_dir = "data/garbage_classification_split/val"

    train_dataloader , test_dataloader , class_name = setup_data.create_dataloader(train_dir=train_dir,
                                                                                   test_dir=test_dir,
                                                                                   transform=transform,
                                                                                   batch_size=32,
                                                                                   num_workers=os.cpu_count())

    model = model_create.GarbageClassifier().to(device)

    loss_fn = torch.nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(params=model.parameters(),lr=0.0005)

    results = Training_Testing_Engine.train(model,train_dataloader,test_dataloader,loss_fn,optimizer,epochs=20)

    utils.save_model(model,"models","Gargabe_Classification_12.pth")


if __name__ == "__main__":
    main()