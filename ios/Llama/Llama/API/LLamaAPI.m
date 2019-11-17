//
//  LLamaAPI.m
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "LLamaAPI.h"

//NSString * localHostURL = @"http://127.0.0.1:8000/";
//NSString * privateIPURL = @"http://127.0.0.1:8000/";
//NSString * publicURL = @"http://127.0.0.1:8000/";

NSString * localHostURL = @"http://192.168.1.71:8000/";
NSString * privateIPURL = @"http://192.168.1.71:8000/";
NSString * publicURL = @"https://api.ridellama.com/";

NSString * vehicleEndpoint = @"vehicle";

@implementation LLamaAPI

#pragma mark - Vehicle URLs

+(NSString *) interactWithVehicleURL {
    return [NSString stringWithFormat:@"%@%@/%@", [self apiURL], vehicleEndpoint, @"unlock"];
}

#pragma mark - Base URLs

+(NSString *) apiURL {
    return publicURL;
}

@end
