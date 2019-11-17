//
//  ExploreMapViewController.h
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ExploreMapView.h"
#import "Vehicle.h"

NS_ASSUME_NONNULL_BEGIN

@interface ExploreMapViewController : UIViewController

@property (nonatomic) ExploreMapView * exploreMapView;
@property (nonatomic) Vehicle * vehicle;

@end

NS_ASSUME_NONNULL_END
