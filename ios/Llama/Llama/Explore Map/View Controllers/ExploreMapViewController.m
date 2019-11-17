//
//  ExploreMapViewController.m
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "ExploreMapViewController.h"

@interface ExploreMapViewController ()

@end

@implementation ExploreMapViewController

-(instancetype)init {
    
    if (self = [super init]) {
        [self base_init];
    }
    
    return self;
}

-(void) base_init {
    self.title = @"Explore Map";
    self.exploreMapView = [[ExploreMapView alloc] initWithFrame:self.view.frame];
    
    [self.exploreMapView.activateButton addTarget:self action:@selector(didTapActivateVehicleButton:) forControlEvents:UIControlEventTouchUpInside];
    
    [self.view addSubview:self.exploreMapView];
    
    self.vehicle = [Vehicle new];
}

#pragma mark - Button Event Methods

-(void) didTapActivateVehicleButton: (UIButton *) button {
    
    [self.vehicle interactWithVehicle:YES success:^{
        if (button.selected) {
            [self.exploreMapView setActivateButtonAsDeselected];
        } else {
            [self.exploreMapView setActivateButtonAsSelected];
        }
    } failure:^(NSError * _Nonnull error) {
        
    }];
}

@end
