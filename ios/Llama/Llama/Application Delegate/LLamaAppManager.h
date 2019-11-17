//
//  LLamaAppManager.h
//  Llama
//
//  Created by Caleb Keitt on 11/16/19.
//  Copyright © 2019 com.rider.llama. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface LLamaAppManager : NSObject

-(void)presentRootViewController;

#pragma mark - Singleton App Manager Object

+(LLamaAppManager *) manager;

@end

NS_ASSUME_NONNULL_END
