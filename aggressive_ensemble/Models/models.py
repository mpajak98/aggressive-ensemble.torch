from torchvision import models
import pretrainedmodels

from torch import nn

__all__ = ['resnet50', 'resnet152', 'alexnet', 'vgg', 'densenet',
           'inceptionV3', 'xception', 'nasnetalarge', 'nasnetamobile']


def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False


def nasnetalarge(num_classes, feature_extract, use_pretrained=True):

    model = pretrainedmodels.nasnetalarge(num_classes=num_classes, pretrained='imagenet')
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.last_linear.in_features
    model.last_linear = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]

    return model, input_size, mean, std


def nasnetamobile(num_classes, feature_extract, use_pretrained=True):
    model = pretrainedmodels.nasnetamobile(num_classes=num_classes, pretrained='imagenet')
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.last_linear.in_features
    model.last_linear = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]

    return model, input_size, mean, std


def xception(num_classes, feature_extract, use_pretrained=True):

    model = pretrainedmodels.xception(num_classes=num_classes, pretrained='imagenet')
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.last_linear.in_features
    model.last_linear = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 299
    mean, std = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]

    return model, input_size, mean, std


def inceptionV3(num_classes, feature_extract, use_pretrained=True):

    model = models.inception_v3(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    # Handle the auxilary net
    num_ftrs = model.AuxLogits.fc.in_features
    model.AuxLogits.fc = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    # Handle the primary net
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 299
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std


def densenet(num_classes, feature_extract, use_pretrained=True):

    model = models.densenet121(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.classifier.in_features
    model.classifier = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std


def vgg(num_classes, feature_extract, use_pretrained=True):

    model = models.vgg11_bn(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.classifier[6].in_features
    model.classifier[6] = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std


def alexnet(num_classes, feature_extract, use_pretrained=True):

    model = models.alexnet(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.classifier[6].in_features
    model.classifier[6] = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std


def resnet50(num_classes, feature_extract, use_pretrained=True):
    
    model = models.resnet50(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std


def resnet152(num_classes, feature_extract, use_pretrained=True):

    model = models.resnet152(pretrained=use_pretrained)
    set_parameter_requires_grad(model, feature_extract)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, num_classes),
        nn.Sigmoid())
    input_size = 224
    mean, std = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]

    return model, input_size, mean, std
