//
//  ExploreMapView.h
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

@interface ExploreMapView : UIView

-(void) setActivateButtonAsSelected;
-(void) setActivateButtonAsDeselected;

@property (nonatomic) UIButton * activateButton;

@end

NS_ASSUME_NONNULL_END
