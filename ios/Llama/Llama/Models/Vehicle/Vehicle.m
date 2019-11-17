//
//  Vehicle.m
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "Vehicle.h"

@implementation Vehicle

#pragma mark - API Calls

-(void) interactWithVehicle: (BOOL) unlock success: (void (^) (void)) success  failure: (void (^) (NSError * error)) failure {
    
    NSError * error;
    NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
    
    AFURLSessionManager * manager = [[AFURLSessionManager alloc] initWithSessionConfiguration:configuration];
    
    NSMutableURLRequest * request = [[AFJSONRequestSerializer serializer] requestWithMethod:@"POST" URLString:[LLamaAPI interactWithVehicleURL] parameters:@{@"qr_verification_code" : @"990447029699624"} error:&error];
    
    NSURLSessionDataTask * dataTask = [manager dataTaskWithRequest:request uploadProgress:nil downloadProgress:nil  completionHandler:^(NSURLResponse * _Nonnull response, id  _Nullable responseObject, NSError * _Nullable error) {
        dispatch_async(dispatch_get_main_queue(), ^{
            if (error) {
                failure(error);
            } else {
                success();
            }
        });
    }];
        
    [dataTask resume];
}

@end
