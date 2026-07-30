import torch
import torchvision


def calculate(y_pred,y_test):
    true = torch.eq(y_pred,y_test).sum().item()

    acc = true / len(y_pred)

    return acc

device = "cuda" if torch.cuda.is_available() else "cpu"

def train_step(model,data,loss_fn,optimizer):
    model.train()

    train_loss = 0
    train_acc = 0

    for X , y in data:
        X = X.to(device)
        y = y.to(device)

        train_logits = model(X)

        loss = loss_fn(train_logits,y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_loss += loss

        y_train_pred_class = torch.argmax(torch.softmax(train_logits , dim=1),dim=1)

        train_acc += calculate(y_train_pred_class , y)

    train_loss = train_loss / len(data)
    train_acc = train_acc / len(data)

    return train_loss , train_acc


def test_step(model,data,loss_fn,optimizer):
    model.eval()

    with torch.inference_mode():
        test_loss = 0
        test_acc = 0
        for X , y in data:
            X = X.to(device)
            y = y.to(device)

            test_logits = model(X)

            test_loss += loss_fn(test_logits,y)

            y_test_pred_class = torch.argmax(torch.softmax(test_logits , dim=1),dim=1)

            test_acc += calculate(y_test_pred_class,y)

        test_loss = test_loss / len(data)
        test_acc = test_acc / len(data)

        return test_loss , test_acc


def train(model,train_data,test_data,loss_fn,optimizer,epochs):

    for epoch in range(epochs):
        train_loss , train_accucary = train_step(model , train_data , loss_fn , optimizer)
        test_loss , test_accuracy = test_step(model , test_data , loss_fn , optimizer)

        print(f"Epoch : {epoch}" f"Train Loss : {train_loss}" f"Train Acc : {train_accucary}" f"Test Loss : {test_loss}" f"Test Acc : {test_accuracy}")