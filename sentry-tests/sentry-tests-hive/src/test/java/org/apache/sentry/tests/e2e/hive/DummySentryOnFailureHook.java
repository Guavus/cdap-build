/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.sentry.tests.e2e.hive;

import junit.framework.Assert;

import org.apache.hadoop.hive.ql.plan.HiveOperation;
import org.apache.sentry.binding.hive.SentryOnFailureHook;
import org.apache.sentry.binding.hive.SentryOnFailureHookContext;

public class DummySentryOnFailureHook implements SentryOnFailureHook {

  public static boolean invoked = false;
  public static boolean checkHiveOp = false;
  public static HiveOperation hiveOp;

  public static void setHiveOp(HiveOperation newHiveOp) {
    checkHiveOp = true;
    hiveOp = newHiveOp;
  }

  @Override
  public void run(SentryOnFailureHookContext failureHookContext)
      throws Exception {
    invoked = true;
    if (checkHiveOp) {
      checkHiveOp = false;
      Assert.assertTrue(hiveOp.equals(failureHookContext.getHiveOp()));
    }
  }
}
