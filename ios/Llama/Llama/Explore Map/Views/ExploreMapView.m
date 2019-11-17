//
//  ExploreMapView.m
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "ExploreMapView.h"

CGFloat EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_HORIZONTAL_MARGIN = 20.0f;
CGFloat EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_HEIGHT = 40.0f;
CGFloat EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_CORNER_RADIUS = 15.0f;

@implementation ExploreMapView

-(instancetype)initWithFrame:(CGRect)frame {
    
    if (self = [super initWithFrame:frame]) {
        [self base_init];
    }
    
    return self;
}

-(void) base_init {
    self.activateButton = [UIButton new];
    self.activateButton.translatesAutoresizingMaskIntoConstraints = NO;
    self.activateButton.backgroundColor = [UIColor systemBlueColor];
    self.activateButton.layer.cornerRadius = EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_CORNER_RADIUS;
    
    [self.activateButton setTitleColor:[UIColor whiteColor] forState:UIControlStateNormal];
    [self.activateButton setTitle:@"ENGAGE" forState:UIControlStateNormal];

    [self.activateButton setTitleColor:[UIColor blackColor] forState:UIControlStateSelected];
    [self.activateButton setTitle:@"ENGAGED!" forState:UIControlStateSelected];
    
    [self addSubview:self.activateButton];
    
    [self layoutActivateButton];
}

-(void) setActivateButtonAsSelected {
    self.activateButton.backgroundColor = [UIColor redColor];
    self.activateButton.selected = YES;
}

-(void) setActivateButtonAsDeselected {
    self.activateButton.backgroundColor = [UIColor blueColor];
    self.activateButton.selected = NO;
}

#pragma mark - Auto Layout Methods

-(void) layoutActivateButton {
    
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self.activateButton
                                                     attribute:NSLayoutAttributeCenterY
                                                     relatedBy:NSLayoutRelationEqual
                                                        toItem:self
                                                     attribute:NSLayoutAttributeCenterY
                                                    multiplier:1.0 constant:0]];
    
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self.activateButton
                                                     attribute:NSLayoutAttributeLeft
                                                     relatedBy:NSLayoutRelationEqual
                                                        toItem:self
                                                     attribute:NSLayoutAttributeLeft
                                                    multiplier:1.0 constant:EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_HORIZONTAL_MARGIN]];
    
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self.activateButton
                                                     attribute:NSLayoutAttributeRight
                                                     relatedBy:NSLayoutRelationEqual
                                                        toItem:self
                                                     attribute:NSLayoutAttributeRight
                                                    multiplier:1.0 constant:-EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_HORIZONTAL_MARGIN]];
    
    [self addConstraint:[NSLayoutConstraint constraintWithItem:self.activateButton
                                                     attribute:NSLayoutAttributeHeight
                                                     relatedBy:NSLayoutRelationEqual
                                                        toItem:nil
                                                     attribute:NSLayoutAttributeHeight
                                                    multiplier:1.0 constant:EXPLORE_MAP_VIEW_ACTIVATE_BUTTON_HEIGHT]];
}

@end
