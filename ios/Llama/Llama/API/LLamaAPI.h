//
//  LLamaAPI.h
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface LLamaAPI : NSObject

+(NSString *) apiURL;

#pragma mark - Vehicle Endpoint
+(NSString *) interactWithVehicleURL;

@end

NS_ASSUME_NONNULL_END
