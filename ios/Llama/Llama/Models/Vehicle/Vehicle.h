//
//  Vehicle.h
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "CoreObject.h"

NS_ASSUME_NONNULL_BEGIN

@interface Vehicle : CoreObject

-(void) interactWithVehicle: (BOOL) unlock success: (void (^) (void)) success  failure: (void (^) (NSError * error)) failure;

@end

NS_ASSUME_NONNULL_END
