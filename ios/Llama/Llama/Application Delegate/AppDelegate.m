//
//  AppDelegate.m
//  Llama
//
//  Created by Caleb Keitt on 11/11/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import "AppDelegate.h"
#import "LLamaAppManager.h"

@interface AppDelegate ()

@end

@implementation AppDelegate


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
    self.window = [[UIWindow alloc] initWithFrame:UIScreen.mainScreen.bounds];
    self.window.backgroundColor = [UIColor whiteColor];
    
    [[LLamaAppManager manager] presentRootViewController];
    
    return YES;
}

@end
