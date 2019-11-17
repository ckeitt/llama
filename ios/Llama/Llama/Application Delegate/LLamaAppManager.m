//
//  LLamaAppManager.m
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "LLamaAppManager.h"
#import "AppDelegate.h"

#import "ExploreMapViewController.h"

@implementation LLamaAppManager

-(void)presentRootViewController {
    
    AppDelegate *appDelegate = (AppDelegate *)[[UIApplication sharedApplication] delegate];
    ExploreMapViewController * exploreMapVC = [[ExploreMapViewController alloc] init];
    appDelegate.window.rootViewController = exploreMapVC;
    [appDelegate.window makeKeyAndVisible];
}

#pragma mark  - Singleton Manager Object

+(LLamaAppManager *) manager {
    
    static LLamaAppManager * manager = nil;
    static dispatch_once_t once_token;
    
    dispatch_once(&once_token, ^{
        manager = [LLamaAppManager new];
    });
    
    return manager;
}

@end
